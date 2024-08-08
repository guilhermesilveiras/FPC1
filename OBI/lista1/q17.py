def conjunto_potencia(conjunto):
    if not conjunto:
        return [set()]
    
    elem = conjunto[0]
    conjunto_restante = conjunto[1:]
    
    subconjuntos_restantes = conjunto_potencia(conjunto_restante)
    
    subconjuntos = []
    for subconjunto in subconjuntos_restantes:
        subconjuntos.append(subconjunto)
        subconjuntos.append(subconjunto | {elem})
    
    return subconjuntos

# Exemplo de uso
conjunto = ['a', 'b', 'c']
resultado = conjunto_potencia(conjunto)
for subconjunto in resultado:
    print(subconjunto)