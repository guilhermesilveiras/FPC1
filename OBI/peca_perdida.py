n = int(input())
pecas = [i for i in range(1, n+1)]
pecasok = [int(x) for x in input().split()]


pecasfaltantes = [i for i in pecas if i not in pecasok]
print(pecasfaltantes[0])