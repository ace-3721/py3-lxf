# -*- coding: utf-8 -*-

print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化

print('Hello, %s' % '世界')
print('你好，%s。你的余额是：¥%d.' % ('张三', 99_999))
print('你好，{0}，你的成绩提升了 {1:.1f}%'.format('小三', 17.125))
r = 2.5
area = 3.14 * r ** 2
print(f'半径为{r}的圆面积是{area:.2f}')
