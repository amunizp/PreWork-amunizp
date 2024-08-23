'''
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3
'''
from Ejercicio2 import lista_divisores 

def esNumeroPerfecto(n):
  divisores = lista_divisores(n)
  if sum(divisores)==n:
    print("es numero perfecto")
    return True
  else:
    print("no es numero perfecto")
    return False

numeroCualquiera=7
print (f'el {numeroCualquiera} es perfecto: {esNumeroPerfecto(numeroCualquiera)}')

numeroCualquiera = int(input("Give me a number and I will tell you if it is a perfect number"))

print (f'el {numeroCualquiera} es perfecto: {esNumeroPerfecto(numeroCualquiera)}')