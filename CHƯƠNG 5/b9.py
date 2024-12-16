import csv

# Dữ liệu
data = [
    ["REGION_ID", "REGION_NAME"],
    [1, "Europe"],
    [2, "Americas"],
    [3, "Asia"],
    [4, "Middle East and Africa"]
]

# Ghi dữ liệu vào file CSV
with open("region.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("File region.csv đã được tạo thành công.")
# doc du lieu ba ng pandas
import pandas as pd
df=pd.read_csv("region.csv")
print(" du lieu trong file region la: ",df)