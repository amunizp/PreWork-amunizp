'''
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
 '''
from Ejercicio1 import comprobar_entero_positivo

def lista_divisores(n):
  n = comprobar_entero_positivo(n)
  i = 1
  listaDivisores=[]
  while i < n:
    if n % i == 0:
      listaDivisores.append(i)
    i+=1
  return listaDivisores

def main():
  print(lista_divisores(10))
  number = int(input("Give me a number and I will give you a list of divisors other than itself: "))
  print(lista_divisores(number))

if __name__ == '__main__':
    main()