import sqlite3
try:
    connection=sqlite3.connect("example.db")
    print("ket noi thanh cong:")
except sqlite3.Error as erros:
    print("loi sau khi ket noi:", erros)
finally:
    if connection:
        connection.close()