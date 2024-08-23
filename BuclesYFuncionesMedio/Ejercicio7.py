'''
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
'''
def doy_num_mayus_minus(texto):
  mayusculas = ''.join(char for char in texto if char.isupper())
  numCapitals = len(mayusculas)
  minusculas = ''.join(char for char in texto if char.islower())
  numLowerCase = len(minusculas)
  return  numCapitals, numLowerCase

mayusculas, minusculas = doy_num_mayus_minus("El Heroe de el Barro.")
print(f'el texto tiene {mayusculas=} y {minusculas=}')

cadena = input("Dame un texto y te cuento mayúsculas y minúsculas: ")

mayusculas, minusculas = doy_num_mayus_minus(cadena)
print(f'el texto tiene {mayusculas=} y {minusculas=}')
