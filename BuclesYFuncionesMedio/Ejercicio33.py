'''
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
import var
def lastElement (thetuple):
  #print(thetuple[-1])
  return thetuple[-1]
def tidyListOfTuples (lstofTuples):
  lstofTuples.sort(key=lastElement)
  return lstofTuples

print(tidyListOfTuples(var.listaDeTuplas2))

print(list(eval('(2,3,4),(1,6,7)')))
lsofT=list(eval(input("give me a list of tuples in this format (2,3),(4,5,6),(3,4,5) with tuples as large as you like. I willorder them according to last tuple\t")))
print(tidyListOfTuples(lsofT))