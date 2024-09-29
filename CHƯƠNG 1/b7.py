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
        print(f"Ngày {self.day:02}/{self.month:02}/{self.year}")
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
if __name__ == "__main__":
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    date = Date(day, month, year)
    print("Ngày hiện tại:")
    date.display()
    date.next()
    print("Ngày tiếp theo:")
    date.display()
