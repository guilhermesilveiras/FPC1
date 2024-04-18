def mega_sena_com_recursividade(numeros, k, i):
    if k == 6:
        print(numeros)
    else:
        for j in range(i, 61):
            numeros[k] = j
            mega_sena_com_recursividade(numeros, k+1, j+1)

#resolver depois