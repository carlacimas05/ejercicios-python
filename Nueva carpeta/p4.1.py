# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:06:49 2023

@author: mar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:13:07 2023

@author: tere

ENUNCIADO:
    Contar pares en una secuencia
    Realizar un script en Python que pida los elementos de una 
    secuencia (de enteros) y obtenga cuántos de sus elementos 
    son números pares.
"""

def contar_numeros_pares(secuencia):
    count = 0
    for num in secuencia:
        if num % 2 == 0:
            count += 1
    return count

def main():
    secuencia = input("Introduzca los números enteros de la secuencia separados por un espacio: ")
    lista_num = list(map(int, secuencia.split()))
    cantidad_pares = contar_numeros_pares(lista_num)
    print(f"La cantidad de números pares en la secuencia es: {cantidad_pares}")

if __name__ == '__main__':
    main()
    
print("Fin del programa")
