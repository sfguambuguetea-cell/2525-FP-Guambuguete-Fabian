# Matriz 3x3 Fabian Fuambuguete
matriz = [
    [450, 125, 980],
    [740, 320, 650],
    [810, 280, 430]
]

#  Escribimos la función Bubble Sort para ordenar una lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    # Copiamos la matriz para no modificar la original
    matriz_ordenada = [fila[:] for fila in matriz]
    matriz_ordenada[fila] = bubble_sort(matriz_ordenada[fila])
    return matriz_ordenada

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la segunda fila (índice 1 por ser base 0)
fila_a_ordenar = 0
matriz_resultado = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz_resultado:
    print(fila)
