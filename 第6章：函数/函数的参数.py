# https://liaoxuefeng.com/books/python/function/parameter/index.html

# 位置参数
#def power(x, n):
    #s = 1
    #while n > 0:
        #n -= 1
        #s *= x
    #return s
#print(power(5, 2))
#print(power(5, 3))

# 默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
print(power(5))
print(power(5, 2))
print(power(5, 3))

def enroll(name, gender, age=6, city='广州'):
    print('姓名：', name)
    print('性别：', gender)
    print('年龄：', age)
    print('城市：', city)
    print('--------')
enroll('张三', '男')
enroll('李四', '女', city='上海')

# 可变参数
def calc(*ns):
    #print(type(ns))
    sum = 0
    for n in ns:
        sum += n
    return sum
print(calc(1, 2, 3))
print(calc(*list(range(101))))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('张三', 16)
person('李四', 23, city='上海')
person('王五', 21, **{'city':'深圳', 'job':'架构师'})

# 命名关键字参数
def car(name, brand, *, price, color):
    print(name, brand, price, color)
car('Q7', '四个圈', price=38, color='灰色')

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99,ext=None)

args = (1, 2, 3, 4)
kw = {'d':99, 'x': '#'}
f1(*args, **kw)

args = (1,2,3)
kw = {'d':88, 'x':'*'}
f2(*args, **kw)
