# 迭代
names = ['张三', '李四', '王五']
for name in names:
    print(name)

sum = 0 
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)


sum = 0
for x in list(range(101)):
    sum += x
print(sum)

# while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
