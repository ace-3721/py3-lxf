# 限制动态绑定的属性
# 对子类无效

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名

s = Student()
s.name = '张三'
s.age = 25
#s.score = 89 # 错误

class GraduateStudent(Student):
    pass

gs = GraduateStudent()
gs.score = 89 # 子类不能继承父类的 __slots__，需要自己定义
