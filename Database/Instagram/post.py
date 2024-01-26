import sqlite3

con = sqlite3.connect('Instagram.db')
print("database connected")
cur = con.cursor()

cur.execute("""CREATE TABLE post(id INTEGER PRIMARY KEY AUTOINCREMENT,
            imageid INTEGER NULL ,
            videoid INTEGER NULL ,
            userid INTEGER NOT NULL ,
            FOREIGN KEY (userid) REFERENCES users(id)
            )""");

print("table created")
con.close()