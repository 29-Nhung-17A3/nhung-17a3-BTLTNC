import sqlite3
connection=sqlite3.connect("ql_nhan_vien.db")
cursor=connection.cursor()
# tao bang phong
cursor.execute("""
CREATE TABLE IF NOT EXISTS PHONG(
Id Integer Primary key,
Name Text Not Null,
Price Real Not Null,
Amount Integer Not Null
)
""")

# tao bang nhan vien
cursor.execute("""
CREATE TABLE IF NOT EXISTS NHAN_VIEN(
id Integer Primary key,
ho_ten Text not Null,
tuoi Integer Not null,
dia_chi Text Not null,
luong Real Not null,
Id_phong Integer Not null,
FOREIGN KEY (id_phong) REFERENCES PHONG(id)
)
""")

def add_department(department_id, department_name):
    connection = sqlite3.connect("ql_nhan_vien.db")
    cursor = connection.cursor()
    
    cursor.execute("""
    INSERT INTO PHONG (id, ten_phong)
    VALUES (?, ?)
    """, (department_id, department_name))
    
    connection.commit()
    print("Phòng ban đã được thêm thành công.")
    connection.close()
def add_employee(employee_id, name, age, address, salary, department_id):
    connection = sqlite3.connect("ql_nhan_vien.db")
    cursor = connection.cursor()
    
    cursor.execute("""
    INSERT INTO NHAN_VIEN (id, ho_ten, tuoi, dia_chi, luong, id_phong)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (employee_id, name, age, address, salary, department_id))
    
    connection.commit()
    print("Nhân viên đã được thêm thành công.")
    connection.close()
def list_employees():
    connection = sqlite3.connect("ql_nhan_vien.db")
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT NV.id, NV.ho_ten, NV.tuoi, NV.dia_chi, NV.luong, P.ten_phong
    FROM NHAN_VIEN NV
    INNER JOIN PHONG P ON NV.id_phong = P.id
    """)
    
    rows = cursor.fetchall()
    
    print("Danh sách nhân viên:")
    for row in rows:
        print(row)
    
    connection.close()