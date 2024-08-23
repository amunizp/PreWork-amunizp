'''
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
'''
#max(set(ls), key=ls.count) falla en test que pasa si todas son únicas? o hay dos de cada? Que pasa si no hay uno más commun que otro?
# no puedo ayudarme de un dicctionario poque la lista puede contener otras listas o diccionarios y eso no lo puedo poner de key.
#No puedo ayudarme de Set por lo mismo.
# normalmente usaría un import math or scipy de algún tipo. 
import var
def deDuplicateList(duplicated_list):
  deduplicated_list = []
  for item in duplicated_list:
    if item not in deduplicated_list:
        deduplicated_list.append(item)
  return deduplicated_list
def most_common_in_list(lst):
  countList   = []
  noDupes = deDuplicateList(lst)
  for item in noDupes:
     countList.append( lst.count(item))
  indexOfMax=[]
  maxnumber = max(countList)
  j=0
  for elem in countList:
    if elem == maxnumber:
      indexOfMax.append(j)
    j+=1
  if len(indexOfMax)==1:
    return noDupes[indexOfMax[0]]
  else:
    return "Hay más de un elemento más común"

def main():

  print("ejercicio 23 elemento mas comun de una lista")
  print(var.lista_cualquiera)
  print(most_common_in_list(var.lista_cualquiera))
  print(var.lista_cualquiera_2)
  print(most_common_in_list(var.lista_cualquiera_2))
  print(var.lista_cualquiera_str)
  print(most_common_in_list(var.lista_cualquiera_str))
  print(var.lista_cualquiera_rara)
  print(most_common_in_list(var.lista_cualquiera_rara))
  
  ls = input("Give me a list of comma separated things and I will find which one is the most common.\t").split(',')
  print(most_common_in_list(ls))

if __name__ == '__main__':
    main()