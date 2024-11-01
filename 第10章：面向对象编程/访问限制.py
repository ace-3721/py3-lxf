class Student(object):
    def __init__(self, name:str, score:int):
        self.set_name(name)
        self.set_score(score)

    def get_name(self) -> str:
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name:str):
        self.__name = name

    def set_score(self, score:int):
        if not ( 0 <= score <= 100 ):
            raise ValueError('成绩错误')
        self.__score = score

    def print_score(self):
        print('%s: %d' % (self.__name, self.__score))

zs = Student('张三', 59)
zs.print_score()
