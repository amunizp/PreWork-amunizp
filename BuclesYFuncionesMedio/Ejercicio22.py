'''
22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
'''
#esto parece una version simplificada de algo que ya hice?

import var
def sumaLista(int_ls):
  laSuma=0
  for n in int_ls:
    laSuma = laSuma + float(n)
  return laSuma


print(sumaLista(var.lista_cualquiera_2))

ls = input('Give me a list of numbers I will add them all ').split(',')
print(sumaLista(ls))
