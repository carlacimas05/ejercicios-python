# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:48:10 2023

@author: mar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:34:32 2023

@author: Candaus
"""

"""
Se parte de una lista inicial explícita dentro del programa y 
una lista vacía, por ejemplo:
lista = [3, 5, 1, 7, 9, 2, 9, 6, 8]
lista_aux = []
Se realizarán las siguientes operaciones:
"""
# 1.     Añadir a lista_aux el último elemento de lista.    
# acceso al índice [-1]


# 2.     Borrar el último elemento de lista.                                                                                          
# método pop()

"""
# 3.     Si lista tiene su valor máximo repetido:                                         
    #función nativa max() y método count()

a.  se eliminará una de las ocurrencias                                                                           
método remove()
b.  se añadirá el máximo a lista_aux                                                                               
método append()
"""

# 4. Se elimina el mínimo de lista. 
# función nativa min() y método remove()

# 5. Se inserta el mínimo anterior en la primera 
# posición de lista_aux.                                  
# método insert()

# 6.Si el último elemento de lista es mayor que el primero, se 
#invertirá el orden de lista.    
# método reverse()

# 7. Se intercambiará el primer elemento con el mínimo de lista.

# 8. Si el valor 2 está en lista se borra 
# de lista y se añade en lista_aux.          
# operador de pertenencia in

# 9. Añade al final de lista_aux la secuencia del 10 al 1.                     
# secuencia range() y método extend()

""" 
10. Sacar por pantalla ambas listas.
Si ha utilizado el ejemplo anterior, la salida por pantalla debería ser:

lista = [9, 6, 7, 5, 3]
lista_aux = [1, 8, 9, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""

lista=[3,5,1,79,2,9,6,8]
lista_aux=[]
#1
lista_aux.append(lista[-1])
#2
lista.pop()
#3
max_valor=max(lista)

if lista.count(max_valor)>1:
    lista.remove(max_valor)
    lista_aux.append(max_valor)
#4
min_valor=min(lista)

lista.remove(min_valor)
#5
lista_aux.insert(0,min_valor)
#6
if lista[-1]>lista[0]:
    lista.reverse()
#7
lista[0], lista[lista.index(min(lista))]=min(lista), lista[0]
#8
if 2 in lista:
    lista.remove(2)
    lista_aux.append(2)
#9  
lista_aux.extend(range(10,0,-1))
#10
print(f"lista= {lista} ")
print(f" lista_aux: {lista_aux} ")

    