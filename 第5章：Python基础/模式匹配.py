score = 'B'

match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')
    case _: # 匹配其他任何情况
        print('谜之成绩')


age = 15

match age:
    case x if x < 10:
        print(f'{x}岁的小屁孩')
    case 10:
        print('你10岁了')
    case 11|12|13|14|15|16|17|18:
        print('粉嫩的小鲜肉')
    case 19:
        print('19岁的你该找工作了')
    case _:
        print('谜之年龄%d' % age)


args = ['gcc', 'hello.c', 'world.c']
#args = ['clean']
#args = ['gcc']

match args:
    case ['gcc']: # 如果只出现gcc，报错
        print('gcc: 缺少源文件')
    case ['gcc', file1, *files]:
        print('gcc 编译：{}, {}'.format(file1, ','.join(files)))
    case ['clean']:
        print('清屏')
    case _:
        print('错误的命令')
