

# Función para calcular temperatura promedio por ciudad
def calcular_promedio(temperaturas, ciudades):
    """
    temperaturas: lista 4D con dimensiones [ciudad][semana][día][momento]
    ciudades: lista con nombres de las ciudades
    """
    promedios = {}

    for i, ciudad in enumerate(ciudades):
        suma = 0
        conteo = 0

        # recorrer semanas, días y momentos
        for semana in temperaturas[i]:
            for dia in semana:
                for temp in dia:
                    suma += temp
                    conteo += 1

        promedio = suma / conteo if conteo > 0 else 0
        promedios[ciudad] = promedio

    return promedios


#  EJEMPLO DE USO
ciudades = ["Loja", "Ambato", "Manabí"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
momentos = ["Mañana", "Tarde", "Noche"]

# Datos simulados: 3 ciudades x 4 semanas x 7 días x 3 momentos
temperaturas = [
    [   # Loja
        [   # Semana 1
            [15, 22, 18], [16, 23, 19], [15, 24, 20], [14, 25, 18],
            [15, 22, 19], [16, 23, 20], [14, 21, 18]
        ],
        [   # Semana 2
            [16, 23, 18], [15, 22, 19], [14, 24, 20], [15, 25, 19],
            [14, 21, 18], [16, 23, 20], [15, 22, 19]
        ],
        [   # Semana 3
            [14, 21, 18], [16, 23, 20], [15, 24, 19], [14, 25, 18],
            [16, 22, 19], [15, 23, 20], [14, 21, 18]
        ],
        [   # Semana 4
            [15, 22, 19], [16, 23, 18], [15, 24, 20], [14, 25, 19],
            [15, 22, 18], [16, 23, 20], [14, 21, 19]
        ]
    ],
    [   # Ambato
        [
            [12, 20, 15], [13, 21, 16], [12, 22, 15], [14, 23, 17],
            [13, 20, 15], [12, 21, 16], [13, 22, 17]
        ]
    ] * 4,  # Repetimos los datos 4 semanas
    [   # Manabí
        [
            [22, 30, 25], [23, 31, 26], [22, 32, 27], [24, 33, 26],
            [23, 31, 25], [22, 30, 26], [24, 32, 27]
        ]
    ] * 4
]

# Calcular promedios
promedios = calcular_promedio(temperaturas, ciudades)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f}°C")
