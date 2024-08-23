'''
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
'''
def esPrimo(n):
  if n <= 0 or not isinstance(n, int) :
    print("tiene que ser numero positivo sin decimales", n, "no vale.")
  elif n== 1 or n == 2 :
    return True
  else:
    i=2
    sqn = n **0.5
    #https://en.wikipedia.org/wiki/Primality_test
    while i <=sqn:
      if n % i == 0:
        return False
        break
      i +=1
      if i > sqn :
        return True

def lista_de_primeros_primos(n):
  listaDePrimos=[]
  i=1
  while len(listaDePrimos)<n:
    if esPrimo(i):
      listaDePrimos.append(i)
    i+=1
  return listaDePrimos

def main():
  print(lista_de_primeros_primos(5))
  n = int(input("Give me the quantity of primes you want "))
  print (lista_de_primeros_primos(n))

if __name__ == '__main__':
    main()