import sqlite3
connection=sqlite3.connect("example.db")
print("phien ban sql:",sqlite3.sqlite_version)
connection.close()