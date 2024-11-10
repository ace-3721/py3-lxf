'''
try:
    f = open('./文件操作.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''

'''
with open('./文件操作.py', 'r', encoding='utf-8') as f:
    #print(f.read())
    for line in f.readlines():
        #print(line.strip())
        print(line)
'''


with open('/tmp/foobar.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, 世界！')
