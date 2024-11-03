class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, v:int):
        if v < 0 or v > 100:
            raise ValueError('成绩应介于1~100')
        self._score = v
        return

    # 只读属性
    @property
    def age(self):
        return 99


s = Student()
s.score = 55
print(s.score)
# s.age = 12 # 只读属性
print(s.age)

# 练习
#  请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, w:int):
        self._width = w

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, h:int):
        self._height = h

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
