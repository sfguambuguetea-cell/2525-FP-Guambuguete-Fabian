# Aplicacion de temperaturas Fabian Guambuguete

# Ciudades
ciudades = ["Loja", "Ambato", "Manabí"]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Momentos del día
momentos = ["Mañana", "Tarde", "Noche"]

# Crear una matriz 3D de temperaturas (ciudad x día x momento)
# Inicialmente con valores de ejemplo
temperaturas = [
    [   # Loja
        [15, 22, 18],   # Lunes
        [16, 23, 19],   # Martes
        [15, 24, 20],   # Miércoles
        [14, 25, 18],   # Jueves
        [15, 22, 19],   # Viernes
        [16, 23, 20],   # Sábado
        [14, 21, 18]    # Domingo
    ],
    [   # Ambato
        [12, 20, 15],
        [13, 21, 16],
        [12, 22, 15],
        [14, 23, 17],
        [13, 20, 15],
        [12, 21, 16],
        [13, 22, 17]
    ],
    [   # Manabí
        [22, 30, 25],
        [23, 31, 26],
        [22, 32, 27],
        [24, 33, 26],
        [23, 31, 25],
        [22, 30, 26],
        [24, 32, 27]
    ]
]

# Mostrar las temperaturas registradas
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas en {ciudad}:")
    for j, dia in enumerate(dias):
        print(f"  {dia}: ", end="")
        for k, momento in enumerate(momentos):
            print(f"{momentos[k]} {temperaturas[i][j][k]}°C  ", end="")
        print()
