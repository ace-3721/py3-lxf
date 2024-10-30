g = ( x*x for x in range(10))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a,b = b, a + b
        n += 1
    return 'done'
for n in fib(6):
    print(n)
