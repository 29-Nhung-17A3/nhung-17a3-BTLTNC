import numpy as np

#1 Tạo mảng 3x3 chứa các giá trị từ 0 đến 8
arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_1D.reshape((3, 3))
print('arr kích thước 3x3:\n', arr_2D)

#2 Hoán đổi cột 1 và cột 3
arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]
print('chuyển cột 1 sang cột 3 và ngược lại:\n', arr_2D)

#3 Hoán đổi dòng 1 và dòng 2
arr_2D[[0, 1], :] = arr_2D[[1, 0], :]
print('chuyển dòng 1 sang dòng 2 và ngược lại:\n', arr_2D)

#4 Đảo ngược các dòng của mảng
arr_2D = arr_2D[::-1, :]
print('đảo ngược các dòng của arr_2D:\n', arr_2D)

#5 Đảo ngược các cột của mảng
arr_2D = arr_2D[:, ::-1]
print('đảo ngược các cột của arr_2D:\n', arr_2D)

#6 Kiểm tra giá trị rỗng (NaN) trong mảng
arr_2D_null = np.array([[1, 2, 3], [np.nan, 5, 6], [7, np.nan, 9], [4, 5, 6]])  # Sử dụng np.nan thay vì np.NaN
if np.isnan(arr_2D_null).any():
    print('có giá trị rỗng')
else:
    print('không có giá trị rỗng')

#7 Thay thế giá trị NaN bằng 0 và in ra mảng mới
arr_2D_no_null = np.nan_to_num(arr_2D_null)
print('sau khi thay thế NaN bằng 0:\n', arr_2D_no_null)


