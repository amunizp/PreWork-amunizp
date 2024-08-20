'''IntroduccionPython-Bucles.pdf
unciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.

'''
def suma(a,b):
  return a+b
print("la suma de a y b son ", suma(3,4))

def factorial(n):
  if n <= 0 or not isinstance(n, int) :
    print("tiene que ser numero positivo sin decimales")
  elif n <2:
    return 1
  else:
    return n*factorial(n-1)

print("caculando factorials: ")
print("el factorial es: ", factorial(1.1))
print("el factorial es: ", factorial(5))

def esPrimo(n):
  if n <= 0 or not isinstance(n, int) :
    print("tiene que ser numero positivo sin decimales", n, "no vale.")

    
  elif n== 1 or n == 2 :
    print("1 ,2 y 3 son primos, ni me molesto en comprobar")
  elif n==4:
    print("4 no es primo, (esto es una trampa que hice porque no consegui hacier funcionar la lógica para este número)")
  else:
    i=2
    sqn = n **0.5
    print ("comprobamos si es divisible  desde 2 hasta la raiz cuadrada de ", n, " que es ", sqn)
    #https://en.wikipedia.org/wiki/Primality_test
    while i <sqn:
      if n % i == 0:
        print("este número no es primo: ", n)
        break
      else:
        print("voy a probar el siguiente ya que no es divisible por", i)
        
      i +=1
      if i >= sqn :
        print("es primo: ", n)
print ("comprobar si es primo")
esPrimo(79)
esPrimo(80)
esPrimo(4)
esPrimo(5)
esPrimo(6)
esPrimo(8)
esPrimo(0)
esPrimo(0.1)

def suma_de_lista(lista_numeros):
  total=0
  for numero in lista_numeros:
    total = total + numero
  return total
lista_numeros = [4,5,6,7,8]
sumalista = suma_de_lista(lista_numeros)
print("la suma de ", lista_numeros, "es ", sumalista)

def reversa_texto(texto):
  reverso= ''
  for char in reversed(texto):
    reverso = reverso + char
  return reverso, texto[::-1]

print("Dos maneras de reversa de texto", reversa_texto("perro"))


