'''
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
'''
import var
from Ejercicio23 import deDuplicateList
def stringFrequency(chain):
  frequency ={}
  
  for elem in deDuplicateList(list(chain)):
    frequency[elem] = chain.count(elem)
  return frequency

print(stringFrequency(var.random_string))
print(stringFrequency(var.random_string_2))


cadena = input ("Give me some text and I will tell you the frequency of each charecter.\t")
print(stringFrequency(cadena))