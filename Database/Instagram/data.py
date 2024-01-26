import sqlite3

con = sqlite3.connect('Instagram.db')
print("database connected")
cur = con.cursor()

cur.execute("""CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT ,
            image BLOB NULL ,
            video BLOB NULL ) """);

print("table created")
con.close()