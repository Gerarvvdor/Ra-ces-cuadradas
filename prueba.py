from math import *

numeros = []  # Lista que guarda el número inicial
respuesta = ""
numero_cadena = input("Ingrese los números que desea para calcular la raíz: ")

# Convertir los caracteres a números individuales y agregarlos a la lista 'numeros'
for char in numero_cadena:
    numero = int(char)
    numeros.append(numero)

# Verificar si la cantidad de elementos en la lista es par o impar
if len(numeros) % 2 != 0:  # Si es impar
    numeros.insert(0, 0)  # Añadir un 0 al principio de la lista

# Separar los números en parejas y concatenarlos de 2 en 2
numeros_pareados = []  # Lista donde se guardan los pares de números
for i in range(0, len(numeros), 2):
    par = str(numeros[i]) + str(numeros[i + 1])
    numeros_pareados.append(par)

# Operaciones para el primer elemento
operacion_actual = int(numeros_pareados[0])

for i in range(0, 9):
    if (i * i) <= operacion_actual:
        raiz_actual = i
        cuadrado_actual = i * i

operacion_actual -= cuadrado_actual
respuesta = str(raiz_actual)
numeros_pareados.pop(0)

# Bucle para elementos del 01 hasta n
while len(numeros_pareados) > 0:
    operacion_actual = str(operacion_actual) + (numeros_pareados[0])  # se guarda la resta junto con el siguiente par de números
    num_div = operacion_actual  # se guarda el número actual para quitarle el último dígito
    num_div = num_div[:-1]  # se quita el último dígito
    num_div = int(num_div)  # se convierte a entero para poder operar con él
    residuo = floor(num_div / (2 * int(respuesta)))
    if residuo > 10:  # solo se pueden usar raíces del 1 al 9
        residuo = 9

    temp_ans = 2 * int(respuesta)
    temp_ans = str(temp_ans) + str(residuo)  # Concatenando el doble de la raíz actual al residuo
    producto = int(temp_ans) * int(residuo)
    operacion_actual = int(operacion_actual) - int(producto)
    numeros_pareados.pop(0)
    respuesta = respuesta + str(residuo)

# Calculando partes decimales
decimales = ""
for i in range(0, 2):
    cero = 0
    decimales_temp = str(operacion_actual) + str(cero)  # concatenando un cero para poder operar
    decim_residuo = floor(int(decimales_temp) / (2 * int(respuesta)))
    if decim_residuo > 10:  # solo se pueden usar raíces del 1 al 9
        decim_residuo = 9

    decim_temp_ans = 2 * int(respuesta)
    decim_product = int(decim_temp_ans) * int(decim_residuo)
    operacion_actual = int(decimales_temp) - int(decim_product)
    final_decimales = decim_residuo
    decimales += str(final_decimales)

print("La raíz es:", respuesta, ".", decimales)
