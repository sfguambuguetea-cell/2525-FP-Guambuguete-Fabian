# Definimos una matriz 3x3 con valores del 10 al 90 Fabian Guambuguete
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorre filas
        for j in range(len(matriz[i])):   # Recorre columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve posición (fila, columna)
    return None

# Valor a buscar (se puede cambiarlo)
valor_buscado = 20

# escribimos la función
posicion = buscar_valor(matriz, valor_buscado)

# imprimimos resultados
if posicion:
    print(f" El valor {valor_buscado} fue encontrado en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"  El valor {valor_buscado} no se encuentra en a matriz")
