#tentando por insertion sort

prioridades = {'premium': 1, 'diamante': 2, 'ouro': 3, 'prata': 4, 'bronze': 5, 'resto': 6}

def comparar(p1, p2):
    nome1, plano1, gravidade1 = p1
    nome2, plano2, gravidade2 = p2

    if prioridades[plano1] != prioridades[plano2]:
        return prioridades[plano1] - prioridades[plano2]
    if gravidade1 != gravidade2:
        return gravidade1 - gravidade2
    if nome1 < nome2:
        return -1
    if nome1 > nome2:
        return 1
    return 0


def insertion_sort(pacientes):
    for i in range(1, len(pacientes)):
        chave = pacientes[i]
        j = i - 1
        while j >= 0 and comparar(pacientes[j], chave) > 0:
            pacientes[j+1] = pacientes[j]
            j -= 1
            pacientes[j + 1] = chave
    return pacientes

n = int(input())

pacientes = []
for _ in range(n):
    nome, plano, gravidade = input().split()
    gravidade = int(gravidade)
    pacientes.append((nome, plano, gravidade))

pacientes_listados = insertion_sort(pacientes)

for paciente in pacientes_listados:
    print(paciente[0])