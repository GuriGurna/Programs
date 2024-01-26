import sqlite3

conn = sqlite3.connect("Guri.DB")
print("database connected")
cur = conn.cursor()

cur.execute("insert INTO USERS VALUES ('3','guri','1')")
conn.commit()
conn.close()

