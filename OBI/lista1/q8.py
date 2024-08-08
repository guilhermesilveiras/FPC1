# Considere uma partida de futebol entre duas equipes A x B, cujo placar final é m x n, em que m e n são os números de gols marcados por A e B, respectivamente. Implemente um algoritmo recursivo que imprima todas as possíveis sucessões de gols marcados. Por exemplo, para um resultado de 3 x 1 as possíveis sucessões de gols são "A A A B”, "A A B A”, "A B A A" e "B A A A".


def gerar_sucessoes(m, n, sequencia):
    if m == 0 and n == 0:
        print(sequencia)
        return
    
    if m > 0:
        gerar_sucessoes(m - 1, n, sequencia + "A")
    
    if n > 0:
        gerar_sucessoes(m, n - 1, sequencia + "B")

# Exemplo de uso
m = 3
n = 1
gerar_sucessoes(m, n, "")