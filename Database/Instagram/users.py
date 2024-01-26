import sqlite3

con = sqlite3.connect('Instagram.db')
print("database connected")
cur = con.cursor()

cur.execute('''CREATE TABLE Users (id INT PRIMARYKEY AUTO INCREMENT ,
            firstname VARCHAR NOT NULL ,
            lastname VARCHAR NOT NULL ,
            dob DATE , 
            emailid TEXT UNIQUE NOT NULL ,
            phonenumber TEXT UNIQUE ,
            password TEXT NOT NULL ,
            profilepicture BLOB , 
            createdat TIMESTAMP DEAFUT CURRENT_TIMESTAMP , 
            updatedat TIMESTAMP DEFAULT CURRENT_TIMESTAMP )''');

print("table created")
con.close()