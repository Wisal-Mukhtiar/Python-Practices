# comes builtin with python
import sqlite3

conn = sqlite3.connect("db")

c = conn.cursor()

# this command execute the command in the docstrings/ double commas are also acceptable
c.execute("""CREATE TABLE  books(
    BOOK Name text,
    Author text,
    ISBN integer)""")

# sql lite basically has 5 datatypes unlike other databases having dozens of datatypes
# 1. Text
# 2. Integer
# 3. Real
# 4. NULL
# 5. BLOB

# commiting the command
conn.commit()

# closing the connection with the database
conn.close()
