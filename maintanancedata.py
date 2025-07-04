import sqlite3

con=sqlite3.connect("maintanance.db")
cur=con.cursor()
cur.execute("create table maintanance (date INTEGER,amount INTEGER,description TEXT)")
con.commit()
con.close()