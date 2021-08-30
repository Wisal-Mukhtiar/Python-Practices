import sqlite3

conn = sqlite3.connect("db")

c = conn.cursor()

c.execute("""INSERT INTO root VALUES ('IKIGAI', 112255)""")

print("inserted successfully")

conn.commit()

conn.close()