# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:32:30 2023

@author: mar
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:15:41 2023

@author: tere
ENUNCIADO:
Transformación de un número entero en base b (1<b<=10) 
de N dígitos a base decimal
El programa deberá:
Solicitar la base del número a introducir
Si la base elegida es mayor que 10 o menor que 2, avisar con un 
mensaje de error, volviendo a solicitar la base.
Solicitar un valor entero, exigiendo que sea un valor positivo o 0 
(para simplificar no tendremos en cuenta el signo).
Obtener iteradamente los dígitos que componen el número e 
introducirlos en una lista.
Mostrar por pantalla el contenido de la lista.
Verificar si alguno de los dígitos almacenados en la lista no 
está en el rango [0, base -1]. En ese caso, mostrar un error y finalizar.
Si los dígitos son correctos mostrar por pantalla el equivalente 
decimal.
"""

def base_a_decimal(numero, base):
    decimal = 0
    n = len(numero)
    for i in range(n):
        if numero[i] >= base:
            return -1
        decimal += numero[i] * (base ** (n - i - 1))
    return decimal

while True:
    try:
        base = int(input("Introduce la base del número (entre 2 y 10): "))
        if base < 2 or base > 10:
            print("La base debe estar entre 2 y 10. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("Por favor, introduce un número válido.")

while True:
    try:
        valor = int(input(f"Introduce un número entero en base {base} (positivo o 0): "))
        if valor < 0:
            print("Por favor, introduce un valor positivo o 0.")
        else:
            break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

numero_en_lista = [int(x) for x in str(valor)]
print(f"Contenido de la lista: {numero_en_lista}")

for digito in numero_en_lista:
    if digito >= base:
        print("Error: Alguno de los dígitos está fuera del rango permitido.")
        quit()

resultado_decimal = base_a_decimal(numero_en_lista, base)
if resultado_decimal != -1:
    print(f"El equivalente decimal de {valor} en base {base} es: {resultado_decimal}")
else:
    print("Error: Alguno de los dígitos está fuera del rango permitido.")
