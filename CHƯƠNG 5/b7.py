import sqlite3
connection=sqlite3.connect("example.db")
cursor=connection.cursor()
cursor.execute("""
UPDATE courses SET course_name = 'Advanced Mathematics' WHERE id=1
""")
print("cap nhat thanh cong")
connection.commit()
connection.close()