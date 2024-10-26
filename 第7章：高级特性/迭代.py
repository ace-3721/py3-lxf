# 列表
for x in [1,2,3]:
    print(x)

for idx, val in enumerate(['a', 'b', 'c']):
    print('{}: {}'.format(idx, val))

# 字符串
for c in 'Hello, 世界':
    print(c)

# 字典
d = { 'a':1, 'b':2, 'c': 3}
for key in d:
    print(key)

for val in d.values():
    print(val)

for k,v in d.items():
    print(f"{k}: {v}")

# 判断是否可迭代
from collections.abc import Iterable
print(isinstance('foobar', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(d, Iterable))
print(isinstance(123, Iterable))

# 引用多个
for x, y in [(1,1), (2,4), (3,9)]:
    print(x,y)

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])
    min,max = L[0], L[-1]
    for n in L:
        if n < min:
            min = n
        if n > max:
            max = n
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
