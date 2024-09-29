import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
    def display(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

class Ellipse(Point):
    def __init__(self, x, y, major_axis, minor_axis):
        super().__init__(x, y)
        self.major_axis = major_axis 
        self.minor_axis = minor_axis   

    def area(self):
        return math.pi * self.major_axis * self.minor_axis 
    def display(self):
        super().display()
        print(f"Bán trục lớn: {self.major_axis}")
        print(f"Bán trục nhỏ: {self.minor_axis}")
        print(f"Diện tích elip: {self.area()}")
class Circle(Ellipse):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)
    def display(self):
        super().display() 
if __name__ == "__main__":
    print("Nhập thông tin cho elip:")
    x = float(input("Nhập tọa độ x của tâm elip: "))
    y = float(input("Nhập tọa độ y của tâm elip: "))
    major_axis = float(input("Nhập bán trục lớn: "))
    minor_axis = float(input("Nhập bán trục nhỏ: "))
    
    ellipse = Ellipse(x, y, major_axis, minor_axis)
    ellipse.display()
    print("\nNhập thông tin cho đường tròn:")
    radius = float(input("Nhập bán kính: "))   
    circle = Circle(x, y, radius)
    circle.display()
