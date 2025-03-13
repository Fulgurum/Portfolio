import sqlite3

# Connect to SQLite database
def fetch_entries():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, message FROM guestbook ORDER BY id DESC")
    entries = cursor.fetchall()
    conn.close()
    return entries

# Generate HTML output
print("Content-type: text/html\n")
print("<div class='guestbook-messages'>")
entries = fetch_entries()
if entries:
    for name, message in entries:
        print(f"<div class='entry'><strong>{name}</strong>: {message}</div>")
else:
    print("<p>No entries yet. Be the first to sign the guestbook!</p>")
print("</div>")
