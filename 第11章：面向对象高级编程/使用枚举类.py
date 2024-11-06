from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# ------- 

@unique
class Weekday(Enum):
    Sun = 0 # Sun 的 value 设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# -----
# 练习 把Student的gender属性改造为枚举类型，可以避免使用字符串

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name:str, gender:Gender):
        self.name = name
        self.gender = gender

zs = Student('张三', Gender.Male)
if zs.gender == Gender.Male:
    print('测试通过')
else:
    print('测试失败')
