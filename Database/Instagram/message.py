import sqlite3

con = sqlite3.connect('Instagram.db')
print("database connected")
cur = con.cursor()

cur.execute("""CREATE TABLE message (id INTEGER PRIMARY KEY AUTOINCREMENT ,
            senderid INTEGER ,
            recieverid INTEGER, 
            senttime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            seen BOOLEAN ,
            text TEXT NULL, 
            videoid INTEGER NULL,
            imageid INTEGER NULL,
            postid INTEGER NULL,
            FOREIGN KEY (senderid) REFERENCES users (id),
            FOREIGN KEY (recieverid) REFERENCES users(id),
            FOREIGN KEY (videoid) REFERENCES data(id)
            FOREIGN KEY (imageid) REFERENCES data(id)
            FOREIGN KEY (postid) REFERENCES post(id))""")

print("tablecreated")
con.close()