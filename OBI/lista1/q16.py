def unir_arrays(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    return [arr1[0]] + unir_arrays(arr1[1:], arr2)

# Exemplo de uso
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(unir_arrays(arr1, arr2))  # Saída: [1, 3, 5, 2, 4, 6]