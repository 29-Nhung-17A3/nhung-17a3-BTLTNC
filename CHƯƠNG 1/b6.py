class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.stack = []           
        self.top = -1            
    def isFull(self):
        return self.top == self.capacity - 1
    def isEmpty(self):
        return self.top == -1
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value) 
            self.top += 1            
            print(f"Đã thêm {value} vào ngăn xếp.")
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()  
            self.top -= 1            
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value
    def count(self):
        return self.top + 1 
    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp (từ đáy lên đỉnh):")
            for item in self.stack:
                print(item)
    def __del__(self):
        del self.stack                
if __name__ == "__main__":
    capacity = int(input("Nhập sức chứa của ngăn xếp: "))
    s = Stack(capacity)
    while True:
        print("\nChọn hành động:")
        print("1. Thêm phần tử vào ngăn xếp (push)")
        print("2. Lấy phần tử từ ngăn xếp (pop)")
        print("3. Kiểm tra ngăn xếp có rỗng không (isEmpty)")
        print("4. Kiểm tra ngăn xếp có đầy không (isFull)")
        print("5. Đếm số phần tử trong ngăn xếp (count)")
        print("6. In nội dung ngăn xếp (print_stack)")
        print("7. Thoát")        
        choice = int(input("Lựa chọn của bạn: "))       
        if choice == 1:
            value = float(input("Nhập phần tử (float) cần thêm: "))
            s.push(value)
        elif choice == 2:
            s.pop()
        elif choice == 3:
            if s.isEmpty():
                print("Ngăn xếp đang rỗng.")
            else:
                print("Ngăn xếp không rỗng.")
        elif choice == 4:
            if s.isFull():
                print("Ngăn xếp đã đầy.")
            else:
                print("Ngăn xếp chưa đầy.")
        elif choice == 5:
            print(f"Số phần tử hiện tại trong ngăn xếp: {s.count()}")
        elif choice == 6:
            s.print_stack()
        elif choice == 7:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
