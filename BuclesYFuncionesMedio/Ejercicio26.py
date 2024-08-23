'''
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
'''
import var

def nonCommonFromLists(lst1, lst2):
  list2No1=[elem for elem in lst2 if elem not in lst1]
  list1No2 =[elem for elem in lst1 if elem not in lst2]
  return list2No1+list1No2

print(f'lo que no tiene en commun {var.lista_cualquiera=} y {var.lista_cualquiera_2=} es {nonCommonFromLists(var.lista_cualquiera, var.lista_cualquiera_2)}')
print(f'lo que no tiene en commun es {nonCommonFromLists([1,2], [3, 4])}')

ls1 = input("Give me a list\t").split(',')
ls2 = input("Give me a list\t").split(',')
print(f'What they don´t have in common is {nonCommonFromLists(ls1, ls2)}')

