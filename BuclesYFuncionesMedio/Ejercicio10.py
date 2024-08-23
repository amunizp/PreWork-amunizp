'''
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''
lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]
lista_cualquiera_2 = [3, 4, 5, 6, 2, 5]
def encuentra_Interseccion (lista1, lista2):
  interseccion= []
  print("Buscando cosas en comun entre", lista1, lista2)
  for elem in lista1:
    if lista2.count(elem) >0:
      interseccion.append(elem)
      #podia haber ido comprobando uno a uno a ver si es duplicado pero considere que es más eficiente buscar los duplicados luego. Si no usaría un nestes if y luego comprobar el contains. 

  return list(dict.fromkeys(interseccion)) 
print(encuentra_Interseccion(lista_cualquiera, lista_cualquiera_2))

ls1= input("Give me a list (comma separated) to cross check and find the intersection: ").split(',')
ls2= input("Give me a list  (comma separated) to cross check and find the intersection: ").split(',')
print(encuentra_Interseccion(ls1, ls2))

