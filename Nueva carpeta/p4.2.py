# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:28:51 2023

@author: mar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:13:57 2023

@author: tere
ENUNCIADO:
    Determinar si un entero es capicúa

Para determinar si un número entero es capicúa, podemos 
extraer iterativamente la cifra menos significativa (unidades) 
del número usando los operadores % y //. Iremos almacenando 
dichas cifras, según las vayamos obteniendo, en una lista. 
Para determinar si el número es capicúa, recorreremos simultáneamente la lista desde el inicio y desde el final. Si detectamos que los dígitos son diferentes sabremos que el número no es capicúa.

El programa deberá:

Solicitar el valor entero, exigiendo que sea un valor positivo ó 0.
Obtener iteradamente los dígitos que componen el número e 
introducirlos en una lista.
Mostrar por pantalla la lista.
Determinar si el número es capicúa analizando la lista obtenida.
Mostrar por pantalla si el número es o no capicúa.
"""





def es_capicua(numero):
    numero_str = str(numero)
    lista_digitos = [int(digito) for digito in numero_str]
    print(f"Lista de dígitos: {lista_digitos}")
    longitud = len(lista_digitos)
    for i in range(longitud // 2):
        if lista_digitos[i] != lista_digitos[longitud - i - 1]:
            return False
    return True

while True:
    try:
        valor = int(input("Introduce un número entero positivo o 0: "))
        if valor < 0:
            print("Por favor, introduzca un valor positivo o 0.")
        else:
            break
    except ValueError:
        print("Por favor, introduzca un número entero válido.")

if es_capicua(valor):
    print(f"El número {valor} es capicúa.")
else:
    print(f"El número {valor} no es capicúa.")
