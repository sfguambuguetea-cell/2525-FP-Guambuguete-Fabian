# Tarea: Trabajando con Diccionarios en Python Fabian Guambuguete

# Mi_diccionario
#Crear un diccionario con información personal
diccionario = {
    "Nombre": "Agustin",

    "Apellido": "Aroca ",

    "Edad": 65,

    "Email": "agustaro@gmail.com",

    "Ciudad": "Quito",

     "Profesión": "Maestro constructor"

}

#Acceder y modificar el valor de la clave "ciudad"

diccionario ["Ciudad"] = "Quito"

#Verificar si la clave "telefono existe y agregarla si no

if "Telefono" not in diccionario:

    diccionario ["Teléfono"] = "0997225210"

# Eliminar la clave "edad"

del diccionario["Edad"]

#Imprimir el diccionario final

print(diccionario)