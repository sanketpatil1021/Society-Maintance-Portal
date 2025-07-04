import sqlite3

con=sqlite3.connect("flat.db")
cur=con.cursor()
cur.execute("create table flat(id INTEGER PRIMARY KEY AUTOINCREMENT,flat_no INTEGER,owner_name TEXT,contact_no INTEGER,alternate_contact_no INTEGER)")
con.commit()
con.close()

