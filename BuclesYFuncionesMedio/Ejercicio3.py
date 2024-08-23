'''
3. . Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.

'''



def coje_elementos_unicos(lista):
  unique_list = []
  for element in lista:
    if lista.count(element) == 1:
      unique_list.append(element)
  return unique_list

lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]

print(coje_elementos_unicos(lista_cualquiera))

ls = list(input("Dame una lista separado por comas y yo te la devuelvo los que no se repitan ").split(','))

unicos= coje_elementos_unicos(ls)
print(unicos)