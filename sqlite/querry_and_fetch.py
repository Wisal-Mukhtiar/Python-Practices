import sqlite3

conn = sqlite3.connect("db")

c = conn.cursor()

c.execute("SELECT * FROM root")
# if want to fetch one -> c.fetchone()
# if want to fetch many -> c.fetchmany(4) inside bracket the number of queries one wanna fetch
# if want to fetch all
print(c.fetchall())

conn.commit()

conn.close()