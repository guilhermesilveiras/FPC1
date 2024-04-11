def fib(n):
    if n < 1:
        return 0
    a, b, r = 0, 1, 1
    for i in range(2, n):
        a = b 
        b = r
        r = a + b
    return r

x = int(input())
print(fib(x))