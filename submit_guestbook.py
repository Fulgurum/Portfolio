from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guestbook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def guestbook():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, message FROM guestbook ORDER BY id DESC")
    entries = cursor.fetchall()
    conn.close()
    
    return render_template_string("""
        <html><body>
        <h1>Guestbook</h1>
        <form action="/submit" method="post">
            Name: <input type="text" name="name" required><br>
            Message: <textarea name="message" required></textarea><br>
            <input type="submit" value="Sign Guestbook">
        </form>
        <h2>Entries:</h2>
        {% for name, message in entries %}
            <p><strong>{{ name }}</strong>: {{ message }}</p>
        {% endfor %}
        </body></html>
    """, entries=entries)

@app.route("/submit", methods=["POST"])
def submit_guestbook():
    name = request.form.get("name")
    message = request.form.get("message")

    if name and message:
        conn = sqlite3.connect("guestbook.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO guestbook (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        return "Error: Name and message are required."

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)
