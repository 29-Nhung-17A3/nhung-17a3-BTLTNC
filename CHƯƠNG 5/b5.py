import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Tạo bảng nếu chưa có
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
)
""")

# Chèn bản ghi
courses = [("Mathematics",), ("Physics",), ("Chemistry",)]
cursor.executemany("INSERT INTO courses (course_name) VALUES (?)", courses)
print("Thêm các bản ghi thành công.")

connection.commit()
connection.close()