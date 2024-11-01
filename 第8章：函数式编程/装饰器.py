'''
def log(fn):
    def wrapper(*args, **kw):
        print('调用 %s():' % fn.__name__)
        return fn(*args, **kw)
    return wrapper

@log
def now():
    print('2024-11-1')

now()
'''

def log(text):
    def decorator(fn):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator

@log('执行')
def now():
    print('2024-11-1')

now()
