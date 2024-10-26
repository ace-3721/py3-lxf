print( [x * x for x in range(1,11)] )

print( [x * x for x in range(1,11) if x % 2 == 0] )

print( [m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件
import os
print( [d for d in os.listdir('.')] )

# 字典
d = {'name':'张三', 'age':23, 'city':'广州'}
print( [f'{k}={v}' for k,v in d.items() ])

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
