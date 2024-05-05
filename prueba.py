from math import floor
from math import *
numbers = [] #Lista que guarda el número inicial
answer = ""
number_string = input("Ingrese los números que desea para calcular la raiz: ")

# Convertir los caracteres a números individuales y agregarlos a la lista 'numbers'
for char in number_string:
    number = int(char)
    numbers.append(number)

# Verificar si la cantidad de elementos en la lista es par o impar
if len(numbers) % 2 != 0:  # Si es impar
    numbers.insert(0, 0)  # Añadir un 0 al principio de la lista

# Separar los números en parejas y concatenarlos de 2 en 2
paired_numbers = [] #Lista donde se guardan los pares de numeros
for i in range(0, len(numbers), 2):
    pair = str(numbers[i]) + str(numbers[i + 1])
    paired_numbers.append(pair)


def count_elements(lst):
    return len(lst)

print("Cantidad de elementos en la lista paired_numbers:", count_elements(paired_numbers))

for number in paired_numbers:
    print(number)

print("Inciando calculo de raiz del número :)")


#Operaciones para el primer elemento
operacion_actual = int(paired_numbers[0])
print("Primera operación:", operacion_actual)

for i in range(1,10):
    if (i*i) <= operacion_actual:
        actual_square = i
        actual_cuad = i*i
  
print("Raiz inicial:", actual_square, " Cuadrado a usar:", actual_cuad)

# Restando el cuadrado a la operación actual
operacion_actual -= actual_cuad
answer = str(actual_square)
# Eliminar el primer elemento de paired_numbers
paired_numbers.pop(0)

# Bucle para elementos del array del 01 hasta n
while len(paired_numbers) > 0:
    operacion_actual = str(operacion_actual) + (paired_numbers[0]) #se guarda la resta junto con el siguiente par de números
    print("Resta actual: ", operacion_actual)
    operacion_actual = float(operacion_actual) #se convierte a entero
    num_div = operacion_actual #se guarda el número actual para quitarle el último dígito
    num_div = str(num_div)
    num_div = num_div[:-1] #se quita el último dígito
    num_div = float(num_div) #se convierte a entero para poder operar con él
    print("Numero sin el último",num_div)
    residuo = floor(num_div/(2*int(answer))) #se divide el número sin el último dígito entre el doble de la respuesta actual
    if residuo > 10:
        residuo = 9
    else:
        residuo

    print("Residuo: ", residuo)
    temp_ans = str(2*answer) + str(residuo) #Concatenando el doble de la raiz actual al residuo
    print("Numero actual a multiplicar el residuo: ", temp_ans)
    operacion_actual = int(operacion_actual)  #convirtiendo a entero el numero a dividor
    print("Número con residuo: ", operacion_actual)
    producto = float(temp_ans) * residuo #se multiplica el doble de la respuesta actual por el residuo

    operacion_actual -= producto #poniendo un comentario random
    print("Después de resta: ",operacion_actual)
    paired_numbers.pop(0)
    answer += str(residuo)

print("Respuesta final:", answer)
print("Raiz cuadrada de ", number_string, " es: ", answer)