#def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#        return -x

from abstest import my_abs
print(my_abs(-99))


# 空函数
def nop():
    pass

# 参数检查
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    return -x
#print(my_abs1('a'))

# 返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(f'移动到：{x}, {y}')
