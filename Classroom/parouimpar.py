# Dois amigos, Alice e Bob, estão jogando um jogo muito simples, em que um deles grita ou “par” ou “ímpar” e o outro imediatamente responde ao contrário, respectivamente “ímpar” ou “par”. Em seguida, ambos exibem ao mesmo tempo uma mão cada um, em que alguns dedos estão estendidos e outros dobrados. Então eles contam o número total de dedos estendidos. Se a soma for par, quem gritou “par” ganha. Se a soma for ímpar, quem gritou “ímpar” ganha. Por exemplo, suponhamos que a Alice gritou “par” e o Bob respondeu “ímpar”. Em seguida, Alice não deixou nenhum dos seus dedos estendidos, ao passo que Bob deixou três dedos estendidos. A soma então é três, que é ímpar, portanto Bob ganhou. Seu programa deve determinar quem ganhou, tendo a informação de quem gritou par e o número de dedos estendidos de cada um.

# Entrada
# A entrada contém três linhas, cada uma com um número inteiro, P, D1 e D2, nesta ordem. Se P = 0 então Alice gritou “par”, ao passo que se P = 1 então Bob gritou “par”. Os números D1 e D2 indicam, respectivamente, o número de dedos estendidos da Alice e do Bob.

# Saída
# Seu programa deverá imprimir uma única linha, contendo um único número inteiro, que deve ser 0 se Alice foi a ganhadora, ou 1 se Bob foi o ganhador.

# Restrições
# • P = 0 ou P = 1
# • 0 ≤ D1 ≤ 5
# • 0 ≤ D2 ≤ 5


P = int(input(''))
D1 = int(input(''))
D2 = int(input(''))

if D1 < 0 or 5 < D1 or D2 < 0 or 5 < D2:
    print('Error')

if P == 0 and (D1+D2) %2 == 0:
    print('0')
elif P == 0 and (D1+D2) % 2 != 0:
    print('1')
elif P == 1 and (D1+D2) %2 == 0:
    print('1')
else:
    print('0')