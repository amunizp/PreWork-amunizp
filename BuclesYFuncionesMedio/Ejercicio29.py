'''
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
'''

def average_of_list (lst):
  lst=list(map(float,lst))
  return round(sum(lst)/len(lst),2)


lista_cualquiera_num = [1,2,1,-2,2,2.4,3]
print(average_of_list(lista_cualquiera_num))
print(average_of_list([1,2,3]))

ls = input('Give me a list of numbers separated by comma and I will return average\t').split(',')
print(average_of_list(ls))