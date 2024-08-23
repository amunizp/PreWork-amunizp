'''
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
'''
from Ejercicio1 import comprobar_entero_positivo

def fibonacci_2 (n):
  n = comprobar_entero_positivo(n)
  if n ==0:
    return [0]
  elif n==1:
    return [0, 1]
  else: 
    i = 2
    a = 0
    b = 1
    fiboList = [0, 1]
    while i <n:
      fiboList.append(a+b)
      c = a + b
      a = b
      b = c
      i+=1
    return fiboList

fibolista = fibonacci_2(3)

print(fibolista)
n = int(input("Give me a number and I will give you it's fibonacci series: "))
print(fibonacci_2(n))