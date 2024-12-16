import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table';
""")
tables = cursor.fetchall()
print("Danh sách bảng:", [table[0] for table in tables])

connection.close()