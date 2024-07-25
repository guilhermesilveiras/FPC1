# Os administradores da Fazenda Fartura planejam criar uma nova plantação de morangos, no formato retangular. Eles têm vários locais possíveis para a nova plantação, com diferentes dimensões de comprimento e largura. Para os administradores, o melhor local é aquele que tem a maior área. Eles gostariam de ter um programa de computador que, dadas as dimensões de dois locais, determina o que tem maior área. Você pode ajudá-los?

#Entrada
#A entrada contém quatro linhas, cada uma contendo um número inteiro. As duas primeiras linhas indicam as dimensões (comprimento e largura) de um dos possíveis locais. As duas últimas linhas indicam as dimensões (comprimento e largura) de um outro possível local para a plantação de morangos. As dimensões são dadas em metros.

#Saída
#Seu programa deve escrever uma linha contendo um único inteiro, a área, em metros quadrados, do melhor local para a plantação, entre os dois locais dados na entrada.

#Restrições
#• 1 ≤ comprimento ≤ 100
#• 1 ≤ largura ≤ 100


area1 = 0
area2 = 0

for i in range(1, 2):
    x = int(input(''))
    y = int(input(''))
    if x < 1 or x > 100 or y < 1 or y > 100:
        print('Error')
        break
    area1 = x * y

for j in range(1, 2):
    x = int(input(''))
    y = int(input(''))
    if x < 1 or x > 100 or y < 1 or y > 100:
        print('Error')
        break
    area2 = x * y

if area1 > area2:
    print(area1)
else:
    print(area2)
    

