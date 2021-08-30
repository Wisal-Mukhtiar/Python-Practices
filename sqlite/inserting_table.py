import sqlite3
conn = sqlite3.connect("db")

c = conn.cursor()

c.execute("SELECT * FROM books WHERE ISBN = 564332 ")

for book in c.fetchall():
    print(book) 