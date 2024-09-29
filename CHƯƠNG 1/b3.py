import math
class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số phải khác 0.")
    def kiem_tra_hop_le(self):
        return self.mau_so != 0
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Phân số không hợp lệ. Mẫu số phải khác 0.")
            self.mau_so = int(input("Nhập lại mẫu số: "))
    def in_phan_so(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        tu_so_rut_gon = self.tu_so // ucln
        mau_so_rut_gon = self.mau_so // ucln
        if mau_so_rut_gon == 1:
            print(f"Phân số: {tu_so_rut_gon}")
        else:
            print(f"Phân số: {tu_so_rut_gon}/{mau_so_rut_gon}")
if __name__ == "__main__":
    phan_so = PhanSo()
    phan_so.nhap_phan_so()
    phan_so.in_phan_so()
