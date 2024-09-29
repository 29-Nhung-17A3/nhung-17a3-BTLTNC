class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def days_in_month(self):
        if self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")
    
    def next(self):
        max_day = self.days_in_month()
        if self.day < max_day:
            self.day += 1
        else:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name                  
        self.birth_date = birth_date     
        self.hire_date = hire_date      
    def display(self):
        print(f"Họ tên nhân viên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.birth_date.display()          
        print("Ngày vào công ty:", end=" ")
        self.hire_date.display()         
if __name__ == "__main__":
    name = input("Nhập họ tên nhân viên: ")
    birth_day = int(input("Nhập ngày sinh: "))
    birth_month = int(input("Nhập tháng sinh: "))
    birth_year = int(input("Nhập năm sinh: "))
    birth_date = Date(birth_day, birth_month, birth_year)
    hire_day = int(input("Nhập ngày vào công ty: "))
    hire_month = int(input("Nhập tháng vào công ty: "))
    hire_year = int(input("Nhập năm vào công ty: "))
    hire_date = Date(hire_day, hire_month, hire_year)
    employee = Employee(name, birth_date, hire_date)
    print("\nThông tin nhân viên:")
    employee.display()
