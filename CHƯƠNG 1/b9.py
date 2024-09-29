class Polygon:
    def __init__(self, num_sides, side_lengths):
        self.num_sides = num_sides  
        self.side_lengths = side_lengths 
    def perimeter(self):
        return sum(self.side_lengths) 
    def display(self):
        print(f"Số cạnh: {self.num_sides}")
        print(f"Các độ dài cạnh: {self.side_lengths}")
        print(f"Chu vi: {self.perimeter()}")
class Parallelogram(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        side_lengths = [base, base, height, height]
        super().__init__(4, side_lengths)  
    def area(self):
        return self.base * self.height  
    def display(self):
        super().display() 
        print(f"Cao: {self.height}")
        print(f"Diện tích: {self.area()}")
class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)  
    def display(self):
        super().display()  
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  
    def display(self):
        super().display()  
if __name__ == "__main__":
    print("Nhập thông tin hình bình hành:")
    base = float(input("Nhập độ dài đáy: "))
    height = float(input("Nhập chiều cao: "))
    parallelogram = Parallelogram(base, height)
    parallelogram.display()
    print("\nNhập thông tin hình chữ nhật:")
    width = float(input("Nhập chiều rộng: "))
    height = float(input("Nhập chiều cao: "))
    rectangle = Rectangle(width, height)
    rectangle.display()
    print("\nNhập thông tin hình vuông:")
    side = float(input("Nhập độ dài cạnh: "))
    square = Square(side)
    square.display()
