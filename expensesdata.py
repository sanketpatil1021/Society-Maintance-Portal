import sqlite3

con=sqlite3.connect("expenses.db")
cur=con.cursor()
cur.execute("create table expenses (fromdate INTEGER,todate INTEGER,amount INTEGER,description TEXT)")
con.commit()
con.close()