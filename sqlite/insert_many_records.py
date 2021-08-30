import sqlite3

conn = sqlite3.connect("db")

c = conn.cursor()

many_books = [
    ('Deep Work', 'Habibi', 564332),
    ('The Archer', 'Paulo Coehlo', 3432),
    ('BRIEF ANSWERS TO THE BIG QUESTION', 'Stephen Hawkings', 342342)
]

# instead of execute, executemany can be written here
c.executemany("INSERT INTO books VALUES(?,?,?)", many_books)

# multiple insertion executed successfully
print("command executed successfully ")

conn.commit()

conn.close()