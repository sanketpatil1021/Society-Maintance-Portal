import sqlite3

con=sqlite3.connect("admin.db")
cur=con.cursor()
#cur.execute("create table admin(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,contact_no INTEGER,email_id TEXT,password INTEGER)")
#cur.execute("create table expenses (fromdate INTEGER,todate INTEGER,amount INTEGER,description TEXT)")
#cur.execute("create table flat(id INTEGER PRIMARY KEY AUTOINCREMENT,flat_no INTEGER,owner_name TEXT,contact_no INTEGER,alternate_contact_no INTEGER)")
cur.execute("create table maintanance (date INTEGER,amount INTEGER,description TEXT)")
con.commit()
con.close()