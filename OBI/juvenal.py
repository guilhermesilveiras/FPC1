def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return F(n/2) + 1
    else:
        return F(3 * n + 1) + 1

def G(n):
    return F(n)

T = int(input())
casos_teste = []

for x in range(T):
    A, B = input().split()
    casos_teste += [(int(A), int(B))]
for A, B in casos_teste:
    max_chamadas = 0
    for i in range(A, B + 1):
        chamadas = G(i)
        if chamadas > max_chamadas:
            max_chamadas = chamadas
    print(f"Caso {x+1} : {max_chamadas}")


