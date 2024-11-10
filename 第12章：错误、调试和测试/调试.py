'''
# 断言
# -O 选项可以关闭断言，即把所有断言视为pass。如：python -O foo.py
def foo(s):
    n = int(s)
    assert n != 0, 'n为零' # 如果断言失败，抛出AssertionError
    return 10 / n
foo('0')
'''

# logging
import logging
logging.basicConfig(level=logging.INFO) #设置日志级别
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
