'''
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.
'''
lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]
lista_cualquiera_2 = [3, 4, 5, 6, 2, 5]
lista_cualquiera_str = ["b", "a", "gato", "abeja", "perro", "pajaro", "esternocleidomastoideo"]

def orderList(lista):
  try:
    lista.sort(reverse=False) 
    return lista
  except TypeError:
    print("Esta lista tiene cosas no comparables, probaste con hacerlo o todo integros o todo texto? ")

print("ordenar una lista cualquiera")
print(lista_cualquiera)
print(orderList(lista_cualquiera))
print("solo un tipo")
print(lista_cualquiera_2)
print(orderList(lista_cualquiera_2))
print(lista_cualquiera_str)
print(orderList(lista_cualquiera_str))
untidyList = input("Give me a list of things separated by commas  and I will tidy them up: ").split(',')
print(orderList(untidyList))