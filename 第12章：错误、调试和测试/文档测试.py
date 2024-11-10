class Dict(dict):
    '''
    简单的字典，但是允许使用 a.b 风格进行访问

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    '''

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' 对象没有 '%s' 属性" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
