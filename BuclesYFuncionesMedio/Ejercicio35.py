'''
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
'''
#hecho como part de ejercicio 31. 

from Ejercicio31 import esPrimo
print("son primos?")
print("67 ",esPrimo(67))
print("4 ", esPrimo(4))
print("9 ", esPrimo(9))

n = int(input("dame un numero te dire True si es primo\t"))
print(esPrimo(n))