'''
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
'''

def add_squares_of_even(n):
  sum =0
  for i in range(n+1):
    if i % 2 ==0:
      sum = sum + i**2 
  return sum

def add_squares_of_even2(n):
  sum =0
  for i in range(0,n,2):
    if i % 2 ==0:
      sum = sum + i**2 
  return sum


print(add_squares_of_even(5))
n= int(input("give me a whole number I will add the squares of all the even numbers up to that number \t"))
print("version 1", add_squares_of_even(n))
print("version 2", add_squares_of_even2(n))