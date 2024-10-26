# 字典
d = {'张三': 95, '李四': 74, '王五': 86}
print(d['张三'])
d['李四'] = 67
print(d['李四'])

#print(d['不存在的KEY']) # 报错
print(d.get('不存在的KEY'))
print(d.get('不存在的KEY', -1))
if '不存在的KEY' in d:
    print(d['不存在的KEY'])
else:
    print('该KEY不存在于字典中')

s = d.pop('李四')
print(s, d)


# 集合
s = {1, 2, 3}
print(type(s), s)
s = set([1,2,3])
print(type(s), s)

for _ in list(range(10)):
    s.add(4)
print(s)

s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print('交集：', s1 & s2);
print('并集：', s1 | s2);
