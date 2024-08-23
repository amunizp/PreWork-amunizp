'''
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
'''
#ya lo habia hecho de muleta arriba cuando set y dictionary me fallaron 
import var
from Ejercicio23 import deDuplicateList
print(deDuplicateList(var.duplicated_list))
#otra manera que me quedó rara:
def deDuplicateList2(duplicated_list):
  singularity =[]
  [singularity.append(item) for item in duplicated_list if item not in singularity] #none none none
  return singularity
print(deDuplicateList2(var.duplicated_list))

ls = input("Give me a list I will de duplicate it\t")
print("method one\t", deDuplicateList(ls))
print("method two\t", deDuplicateList2(ls))

#print(singularity2)