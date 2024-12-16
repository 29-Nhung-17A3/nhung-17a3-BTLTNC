import sqlite3
connection=sqlite3.connect("example.db")
cursor=connection.cursor()
cursor.execute("""
DELETE from courses WHERE id=1
""")
print("cap nhat du lieu thanh cong")
connection.commit()
connection.close()