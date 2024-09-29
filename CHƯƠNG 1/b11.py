import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b 
        self.c = c  
    def perimeter(self):
        return self.a + self.b + self.c  
    def area(self):
        s = self.perimeter() / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) 
    def display(self):
        print(f"Các cạnh tam giác: a={self.a}, b={self.b}, c={self.c}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")
class RightTriangle(Triangle):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)
        super().__init__(self.a, self.b, self.c)  
    def display(self):
        print("Tam giác vuông:")
        super().display()
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        self.a = equal_side 
        self.b = equal_side  
        self.c = base  
        super().__init__(self.a, self.b, self.c) 
    def display(self):
        print("Tam giác cân:")
        super().display()
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, side) 
    def display(self):
        print("Tam giác đều:")
        super().display()
if __name__ == "__main__":
    print("Nhập thông tin cho tam giác:")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))    
    triangle = Triangle(a, b, c)
    triangle.display()
    print("\nNhập thông tin cho tam giác vuông:")
    a = float(input("Nhập cạnh a (cạnh vuông góc): "))
    b = float(input("Nhập cạnh b (cạnh vuông góc): "))    
    right_triangle = RightTriangle(a, b)
    right_triangle.display()
    print("\nNhập thông tin cho tam giác cân:")
    equal_side = float(input("Nhập độ dài cạnh bằng: "))
    base = float(input("Nhập độ dài cạnh đáy: "))
    
    isosceles_triangle = IsoscelesTriangle(equal_side, base)
    isosceles_triangle.display()
    print("\nNhập thông tin cho tam giác đều:")
    side = float(input("Nhập độ dài cạnh: "))    
    equilateral_triangle = EquilateralTriangle(side)
    equilateral_triangle.display()
