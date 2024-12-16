import sqlite3

# Tạo cơ sở dữ liệu và một bảng
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
print("Bảng 'students' được tạo thành công.")

# Đóng kết nối
connection.commit()
connection.close()