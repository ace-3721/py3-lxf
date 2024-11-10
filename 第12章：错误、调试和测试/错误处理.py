'''
try:
    print('try...')
    r = 10 / int('2') 
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')

print('END')
'''

'''
# 记录异常
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
'''

'''
# 抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('无效的值：%s' % s)
    return 10 / n

foo('0')
'''

# 处理之后再抛出
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('无效的值：%s' %s )
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('Value Error!')
        raise # 如果不带参数，就会把当前错误原样抛出

bar()
