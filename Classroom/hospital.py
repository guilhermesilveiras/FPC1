def compara(paciente_1, paciente_2):
    # plano
    if paciente_1[0]>paciente_2[0]:
        return 1
    if paciente_1[0]<paciente_2[0]:
        return -1
    # gravidade
    if paciente_1[1]>paciente_2[1]:
        return 1
    if paciente_1[1]<paciente_2[1]:
        return -1
    # ord. alfabetica
    return 1 if paciente_1[2]<paciente_2[2] else -1
def particao(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if compara(A[j], pivot)==1: #A[j] <= pivot:
            i+=1
            (A[i], A[j]) = (A[j], A[i])
    (A[i+1], A[r]) = (A[r], A[i+1])
    return i+1
def quickSort(A, p, r):
    if p<r:
        pi = particao(A, p, r)
        quickSort(A, p, pi-1)
        quickSort(A, pi+1, r)
dictPlanos = {'premium': 5, 'diamante': 4, 'ouro': 3, 'prata': 2, 'bronze': 1, 'resto': 0}
n = int(input()) # entradas
lista_pacientes=[tuple]*n
for i in range(n):
    lista_temp = [x for x in input().split()]
    lista_temp[0], lista_temp[1], lista_temp[2] = dictPlanos[lista_temp[1]], int(lista_temp[2]), lista_temp[0]
    lista_pacientes[i] = tuple(lista_temp)  
quickSort(lista_pacientes, 0, len(lista_pacientes)-1)
printar = [print(l[2]) for l in lista_pacientes]