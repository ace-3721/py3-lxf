# 查看函数的帮助信息
# help(abs)

# 数据类型转换
print(n := int('123'), type(n))
print(n := int(12.34), type(n))
print(f := float('12.34'), type(f))
print(s := str(1.23), type(s))
print(b := bool(1), type(b))
print(b := bool(None), type(b))

# 练习：请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
m,n = 255, 1000
print(hex(m), hex(n))
