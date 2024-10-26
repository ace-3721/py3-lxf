age = 3
if age >= 6:
    print(f'你好呀，{age}岁的小屁孩')
elif age >= 18:
    print('你%d岁了，已经成年了' % age)
else:
    print('你才%d岁，赶紧去喝奶' % age)


birth = int(input('你是哪年出生的：'))
if birth < 2000:
    print('00前')
else:
    print('00后')


height = 1.75
weight = 80.5
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
elif bmi >= 32:
    print('严重肥胖')
else:
    print('你怕不是外星生物')

