count = 0
def G(contador):
    global count
    count += contador
    return count


def f(n):
    while n != 1:
        if n%2 == 0:
            G(1)
            return f(n/2)
        elif n%2 != 0:
            G(1)
            return f(3*n+1)
    if n == 1:
        return G(0)
        
T = int(input("Digite o número de casos: "))
casos = [int(x) for x in input().split()]

for i in range(T):
    if f(casos[2*i]) > f(casos[2*i+1]):
        print(f'Caso {i+1}: {f(casos[2*i])}')
    else:
        print(f'Caso {i+1}: {f(casos[2*i+1])}')


