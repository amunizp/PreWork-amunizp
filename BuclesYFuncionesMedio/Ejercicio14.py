'''
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
'''
lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]
lista_cualquiera_2 = [3, 4, 5, 6, 2, 5]
lista_cualquiera_str = ["b", "a", "gato", "abeja", "perro", "pajaro", "esternocleidomastoideo"]

def findLongWords (list, n):
  longWords = []
  for element in list:
    wordLength = len(str(element))
    if wordLength > n:
      longWords.append(element)
  return longWords
lista_de_palabras_largas = findLongWords(lista_cualquiera_str, 3)
print(lista_de_palabras_largas)

listaDePalabras = input("Give me a list of words separated by commas: ").split(',')
n = int(input("Tell give me a number and I will give you words longer than that number "))
print(findLongWords(listaDePalabras, n))