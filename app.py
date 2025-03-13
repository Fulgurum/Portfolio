from flask import Flask, request, redirect, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder=".", static_url_path="")

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

@app.route("/guestbook.html")
def guestbook():
    return send_from_directory(".", "guestbook.html")

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
        return redirect("/guestbook.html")
    else:
        return "Error: Name and message are required."

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)
