'''
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
'''
import var

def any_common (lista1, lista2):
  for elem in lista1:
    if lista2.count(elem) >0:
      return True
      break
    
  return False

print(any_common(var.lista_cualquiera, var.lista_cualquiera_2))
print(any_common(var.lista_cualquiera, var.lista_cualquiera_str))

ls1 = input("Give me the fist list (separated by commas) to check to see if something in common\t").split(',')
ls2 = input("Give me the second list (separated by commas) to check to see if something in common\t").split(',')
print(any_common(ls1,ls2))