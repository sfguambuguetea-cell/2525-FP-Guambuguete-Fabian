#Tarea: Parámetros y retorno de valores en funciones Fabian Guambuguete

# Cálculo de Descuento en Compras

# En este programa se utilizo un descuento del 20%
# Definición de la función calcular _ descuento

def calcular_descuento(monto_total, porcentaje_descuento=20):

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


#  Funcionamiento del programa  incluye iva , compra y descuento
IVA = 12 / 100  # 12%

# Primera  compra  (usa el descuento por defecto del 20%)
monto1 = 100.0
descuento1 = calcular_descuento(monto1)
subtotal1 = monto1 - descuento1
iva1 = subtotal1 * IVA
total1 = subtotal1 + iva1


# Salida de resultados primera compra
print("Primera compra:")
print(f" Monto total: ${monto1:.2f}")
print(f" Descuento aplicado: ${descuento1:.2f}")
print(f" Subtotal (descuento aplicado): ${subtotal1:.2f}")
print(f" IVA (12%): ${iva1:.2f}")
print(f" Total a pagar: ${total1:.2f}")



