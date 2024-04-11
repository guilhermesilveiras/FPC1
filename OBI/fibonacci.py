def fib(n):
    if < 1:
        return 0
    a, b, r = 0, 1, 1
    for i in range(2, n+1):
        a = b 
        b = r
        r = a + b
    return r