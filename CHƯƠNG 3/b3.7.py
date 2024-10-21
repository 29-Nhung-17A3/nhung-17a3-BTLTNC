import numpy as np

with open('D:\\DHKL17A3HN\\CHƯƠNG 3\\baseball_2D.txt', 'r', encoding='utf-8-sig') as f:
    a = f.read().strip()  
    a = a.replace('[', '').replace(']', '') 
    a = list(map(int, a.split(','))) 
np_baseball = np.array(a).reshape((1015, 2))  
print(type(np_baseball))  

print(np_baseball[49, :])

np_weight = np_baseball[:, 1]
print(np_weight)

print(np_baseball[123][0])

print('Chiều cao trung bình:', np.mean(np_baseball[:, 0]))
print('Cân nặng trung bình:', np.mean(np_baseball[:, 1]))

correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]

if correlation > 0.5:
    correlation_type = "tương quan thuận mạnh"
elif correlation > 0:
    correlation_type = "tương quan thuận yếu"
elif correlation < -0.5:
    correlation_type = "tương quan nghịch mạnh"
elif correlation < 0:
    correlation_type = "tương quan nghịch yếu"
else:
    correlation_type = "không có tương quan"

print('Hệ số tương quan:', correlation)
print('Kết luận:', correlation_type)
