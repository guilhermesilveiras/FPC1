def maior_saldo_possivel(A, B, saldo):
    saldo = list(saldo)
    for _ in range(B):
        min_index = 0
        for i in range(len(saldo)):
            if saldo[i] < saldo[min_index]:
                min_index = i
        saldo.pop(min_index)
    return ''.join(saldo)

casos = []
while True:
    line = input().strip()
    if not line:
        break
    A, B = map(int, line.split())
    saldo = input().strip()
    casos.append(maior_saldo_possivel(A, B, saldo))

for caso in casos:
    print(caso)