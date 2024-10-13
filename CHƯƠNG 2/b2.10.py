import json
def tinh_tong_nhan_vien(data):
    return sum([don_vi['so_nhan_vien'] for don_vi in data['don_vi']])
def in_thong_tin_cong_ty(data):
    print(f'Tên công ty: {data["ten_cong_ty"]}')
    print(f'Địa chỉ: {data["dia_chi"]}')
def in_thong_ke_don_vi(i, don_vi, tong_nhan_vien):
    ten_don_vi = don_vi['ten_don_vi']
    so_nhan_vien_don_vi = don_vi['so_nhan_vien']
    ty_le = (so_nhan_vien_don_vi / tong_nhan_vien) * 100
    print(f'{i}./ Tên đơn vị: {ten_don_vi}.')
    print(f'   - Số nhân viên: {so_nhan_vien_don_vi}')
    print(f'   - Tỷ lệ: {ty_le:.2f}%.\n')
def thong_ke_nhan_vien(data):
    tong_nhan_vien = tinh_tong_nhan_vien(data)
    in_thong_tin_cong_ty(data)
    print('\n-----Thống kê nhân viên theo đơn vị------')
    for i, don_vi in enumerate(data['don_vi'], 1):
        in_thong_ke_don_vi(i, don_vi, tong_nhan_vien)
if __name__ == '__main__':
    with open('du_lieu.json', 'r') as file:
        du_lieu = json.load(file)
    thong_ke_nhan_vien(du_lieu)