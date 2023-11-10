# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:39:03 2023

@author: mar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:34:18 2023

@author: Candaus
"""

"""
Actualizar un valor de una lista (con repetición)
Se parte de una lista inicial explícita dentro del programa:

lista = [1, 2, 3, 4, 3, 6, 3]
El programa debe solicitar un valor y comprobar si está 
en la lista. Si es así, se actualiza el elemento correspondiente 
de la lista con el valor que decida el usuario 
(introducido con input) y se muestra por pantalla la 
lista modificada. 
En caso contrario, se lanzará un mensaje de error. 
En caso de que el valor aparezca más de una vez 
(como por ejemplo el 3 aparece 3 veces), 
se debe sustituir en todas las posiciones en que aparezca.
"""

lista=[1,2,3,4,3,6,3]
print(f": {lista}")
valor=int(input("introduzca un número para actualizar la lista: "))

if valor in lista:
    nuevo_valor=int(input("Introduzca el nuevo número para actualizar: "))
    for a in range(len(lista)):
        if lista[a]==valor:
            lista[a]= nuevo_valor
            print(F"lista actualizada: {lista} ")
            
else:
    print("error, el valor no se encuentra en la lista")    

print("fin del programa")        