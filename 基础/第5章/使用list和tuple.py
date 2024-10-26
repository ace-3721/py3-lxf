# -*- coding: utf-8 -*-

# 列表
classmates = ['张三', '李四', '王五']
print(classmates)
print('列表长度是(len(classmates))：%d' % len(classmates))
print('列表第一个元素(classmates[0]) = {}'.format(classmates[0]))
print(f'列表最后一个元素(classmates[-1]) = {classmates[-1]}')
classmates.append('赵六')
print('添加赵六(classmates.append(\'赵六\'))之后的列表：', classmates)
classmates.insert(1, '钱七')
print("插入钱七(classmates.insert(1, '钱七'))之后的列表：", classmates)
# https://liaoxuefeng.com/books/python/basic/list-tuple/index.html
