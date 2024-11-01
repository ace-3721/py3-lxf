import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, 世界')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('参数过多')

if __name__ == '__main__':
    test()
