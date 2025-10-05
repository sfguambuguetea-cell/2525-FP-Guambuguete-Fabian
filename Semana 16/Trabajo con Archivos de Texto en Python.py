# Trabajo con Archivos de Texto en Python Fabian Guambuguete

# Escritura de Archivo de Texto

# Abrimos (o creamos) un nuevo archivo llamado "my_notes.txt" en modo escritura ('w')
# Si el archivo ya existe, su contenido será reemplazado.
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales en el archivo
archivo.write("Nota 1: Hoy me levante temprano.\n")
archivo.write("Nota 2: revise mi cuenta de ecuabet.\n")
archivo.write("Nota 3: y como todos los dias me dispuse a jugar .\n")

# Cerramos el archivo después de escribir
archivo.close()


# Lectura de Archivo de Texto

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline()
print("Contenido del archivo my_notes.txt:\n")

# Bucle para leer y mostrar cada línea
linea = archivo.readline()
while linea:
    print(linea.strip())  # strip() elimina saltos de línea al final
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
