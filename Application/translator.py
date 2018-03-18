# Created by: Songshan
import sqlite3

db = sqlite3.connect('D:\GitHub\Labeling-Backend\Application\lkydata.db')
cur = db.cursor()
cur.execute("SELECT * FROM attributes")
rows = cur.fetchall()
 
for row in rows:
    print(row)