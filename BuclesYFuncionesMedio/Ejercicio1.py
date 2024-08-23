'''
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci

'''
def comprobar_entero_positivo (n):
  if n <= 0 or not isinstance(n, int) :
    print("tiene que ser numero positivo sin decimales", n, "no vale.")
  else:
    return n

def fibonacci (n):
  n = comprobar_entero_positivo(n)
  print("Fibonacci 0 is 0")
  print("Fibonacci 1 is 1")
  i = 2
  a = 0
  b = 1
  while i <n:
    print("Fibonacci", i +1 ,"is",  a+b)
    c = a + b
    a = b
    b = c
    i+=1

def main():
  fibonacci(20)
  Numero = int(input("Please give me a positive integer and I will give you that many numbers of a ficonacci sequence: "))
  fibonacci(Numero)

if __name__ == '__main__':
    main()
