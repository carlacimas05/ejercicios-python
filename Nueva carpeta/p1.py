# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:25:38 2023

@author: mar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:33:19 2023

@author: Candaus
"""
"""
Actualizar un elemento de una lista
Se parte de una lista inicial explícita dentro del programa:

lista = [3, 4, 5, 6]
El programa debe solicitar un índice y comprobar si es 
válido (está dentro de los límites de la lista). 
Si es válido, se actualiza el elemento correspondiente 
de la lista con el valor que decida el usuario 
(introducido con input) y se muestra por pantalla 
la lista modificada. En caso contrario, se lanzará un 
mensaje de error.

"""
lista=[3,4,5,6]
índice=int(input("introduzca un índice para actualizar el elemento: "))

if 0<=índice< len(lista):
    nuevo_valor=int(input("introduzca el nuevo valor para el elemento: "))
    lista[índice]=nuevo_valor
    
    print(f"lista actualizada: {lista}")
    
else:
    print("error, índice fuera de los límites de la lista")
    
print("Fin del programa")