
def f(n):
    while n != 1:
        if n%2 == 0:
            return f(n/2)
        elif n%2 !== 0:
            return f(3*n+1)