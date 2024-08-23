'''
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
'''
import var
def reverseList (ls):
  return ls[::-1]
print(var.lista_cualquiera_str)
print(reverseList(var.lista_cualquiera_str))
ls = input("Give me a list separated by commas and I will return it in reverse order \t").split(',')
print(reverseList(ls))