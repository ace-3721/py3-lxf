class Student(object):
    VERSION='1.0.1'

    def __init__(self, name):
        self.name = name
        return


s = Student('张三')
print(s.name, s.VERSION)

print(Student.VERSION)
