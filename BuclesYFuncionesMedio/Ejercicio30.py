'''
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
'''
import var

def findLongWords (lst):
  firstLongestWord=max(lst, key=len)
  lst.remove(firstLongestWord)
  secondLongestWord=max(lst, key=len)
  if len(firstLongestWord)==len(secondLongestWord):
    print("there are at least two longest words I will give you the first one")
  return firstLongestWord

print("longest word in the list ", findLongWords(var.lista_cualquiera_str))
print("longest word in the list ", findLongWords(["gato", "perro", "perra"]))

ls = input("Give me a list of words and I will give you the longest. ").split(',')
print("longest word in the list ", findLongWords(ls))
