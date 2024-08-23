'''
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.

'''
from Ejercicio16 import check_list_only_numbers
import var
def get_second_highest_num(lista):
  print(lista)
  lista = list(map(float, lista))
  if check_list_only_numbers(lista):
    deDuped = list(set(lista))
    deDuped.remove(max(deDuped))
    return max(deDuped)
  else:
    print("Necesito solo números")

print(get_second_highest_num(var.lista_cualquiera_2))

ls = input("Introduce una lista de numeros y you te doy el segundo más grande ").split(',')
print(get_second_highest_num(ls))
