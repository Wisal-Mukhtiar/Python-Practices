import sqlite3

conn = sqlite3.connect("db")

c = conn.cursor()

c.execute("SELECT * FROM books")

# want to print all the objects one by one
items = c.fetchall()
for obj in items:
    print(obj)

# if want to print only the names of the books
for obj in items:
    print("Name of the book : ", obj[0],
          "\nAuthor: ", obj[1],
          "\nisbn: ", obj[2]
          )
    print()

conn.commit()

conn.close()