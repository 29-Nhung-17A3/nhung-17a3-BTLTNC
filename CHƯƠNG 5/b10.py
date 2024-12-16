import sqlite3
connection=sqlite3.connect("product.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT (
               Id Intreger Primary Key,
               Name Text Not null,
               Price Real Not null,
               Amount Integer Not null
)
""")
print("bang da duoc tao thanh cong")
connection.close()

# them san pham
def add_product(produc_id, name, price, amount):
    connection=sqlite3.connect("product.db")
    cursor=connection.cursor()
    cursor.execute("""
    INSERT INTO product (Id, Name, Price, Amount)
    VALUES(?,?,?,?)
    """,(produc_id,name,price,amount))
    connection.commit()
    print("san pham da duoc them thanh cong")
    connection.close()               


# hien thi danh sach san pham
def list_product():
    connection=sqlite3.connect("product.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM product")
    rows=cursor.fetchall()
    print("danh sach san pham la:")
    for row in rows:
        print(row)
    connection.close()
def update_product(product_id, new_name=None, new_price=None, new_amount=None):
    connection = sqlite3.connect("product.db")
    cursor = connection.cursor()
    
    if new_name:
        cursor.execute("UPDATE product SET Name = ? WHERE Id = ?", (new_name, product_id))
    if new_price:
        cursor.execute("UPDATE product SET Price = ? WHERE Id = ?", (new_price, product_id))
    if new_amount:
        cursor.execute("UPDATE product SET Amount = ? WHERE Id = ?", (new_amount, product_id))
    
    connection.commit()
    print("Cập nhật thông tin sản phẩm thành công.")
    connection.close()
def delete_product(product_id):
    connection = sqlite3.connect("product.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    
    connection.commit()
    print("Xóa sản phẩm thành công.")
    connection.close()