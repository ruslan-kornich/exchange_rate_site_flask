import sqlite3
conn = sqlite3.connect("exchage.db")
cursor = conn.cursor()
cursor.execute( "SELECT * FROM xrates")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()