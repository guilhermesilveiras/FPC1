def comprimento_lcs(S: str, T: str) -> int:
    # inicializando a tabela com o caso base
    tabela_pd = [[0 for j in range(len(S)+1)] for i in range(len(T)+1)]
    # execução da pd
    for i in range(1, len(T)+1):
        for j in range(1, len(S)+1):
            if T[i-1] == S[j-1]:
                tabela_pd[i][j] = 1 + tabela_pd[i-1][j-1]
            else:
                tabela_pd[i][j] = max(tabela_pd[i-1][j], tabela_pd[i][j-1])
    print(tabela_pd)
    return tabela_pd[len(T)[len(S)]], tabela_pd

def principal():
    S = 'GUILHERME'
    T = 'HELOISA'
    comprimento_lcs = lcs(S, T)

if __name__ == '__main__':
    print(principal())