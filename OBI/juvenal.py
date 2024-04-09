def f(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return f(n/2)
    elif n%2 != 0:
        return f(3*n+1)
    

p = int(input())
f(p)