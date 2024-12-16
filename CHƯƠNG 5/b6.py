import sqlite3
connection=sqlite3.connect("example.db")
cursor=connection.cursor()
cursor.execute("SELECT COUNT (*) FROM courses")
record_count=cursor.fetchone()[0]
print("so luong ban ghi trong bang courses",record_count)
connection.close()