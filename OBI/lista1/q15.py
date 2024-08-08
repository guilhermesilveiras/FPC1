def mod(x, y):
    if x == y:
        return 0
    elif x < y:
        return x
    else:
        return mod(x - y, y)

# Exemplo de uso
x = 10
y = 3
print(mod(x, y))  # Saída: 1