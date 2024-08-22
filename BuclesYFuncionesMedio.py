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
  print("0, 0")
  print("1, 1")
  i = 2
  a = 0
  b = 1
  while i <n:
    print("fibonacci ", i +1 ,"es",  a+b)
    c = a + b
    a = b
    b = c
    i+=1

fibonacci(20)
'''
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
 '''
 
def lista_divisores(n):
  n = comprobar_entero_positivo(n)
  i = 1
  listaDivisores=[]
  while i < n:
    if n % i == 0:
      listaDivisores.append(i)
    i+=1
  return listaDivisores


print(lista_divisores(10))

'''
3. . Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.

'''



def coje_elementos_unicos(lista):
  unique_list = []
  for element in lista:
    if lista.count(element) == 1:
      unique_list.append(element)
  return unique_list

lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]

print(coje_elementos_unicos(lista_cualquiera))


'''
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.

'''
def sumaDigitos(stringNumber):
  numbersAsLetters = str(stringNumber)
  laSuma=0
  for char in numbersAsLetters:
    laSuma = laSuma + int(char)
  return laSuma

digitosSumados = sumaDigitos(345)
print(digitosSumados)

'''
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''

def cuentaVocales(cadena):
  vocales = ['a', 'e', 'i', 'o' , 'u']
  stringAsList = list(cadena)
  i = 0 
  for vowel in vocales:
    i = i + stringAsList.count(vowel)
  return i
frase = "perro de lucas"
number = cuentaVocales(frase)
print(f"{frase=} tiene este numero {number} de vocales")

'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
'''
def cogeLosPrimeros (list, n):
  return list[0:n+1]

n = 4
primeraparte= cogeLosPrimeros(lista_cualquiera, n)
print(primeraparte)

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

'''
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3
'''

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

'''
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
'''

def devuelve_numero_binario(numero):
  n = comprobar_entero_positivo(numero)
  n_Binario = format(n, "b")
  return n_Binario

numeroCualquiera=6
print(f'El  {numeroCualquiera=} en binario es {devuelve_numero_binario(numeroCualquiera)}')

'''
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''
lista_cualquiera_2 = [3, 4, 5, 6, 2, 5]
def encuentra_Interseccion (lista1, lista2):
  interseccion= []
  print("Buscando cosas en comun entre", lista1, lista2)
  for elem in lista1:
    if lista2.count(elem) >0:
      interseccion.append(elem)
      #podia haber ido comprobando uno a uno a ver si es duplicado pero considere que es más eficiente buscar los duplicados luego. Si no usaría un nestes if y luego comprobar el contains. 

  return list(dict.fromkeys(interseccion)) 
print(encuentra_Interseccion(lista_cualquiera, lista_cualquiera_2))

'''
11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def esPalindromo(cadena):
  cadena = cadena.lower()
  if cadena == cadena[::-1]:
    return True
  else:
    return False

explodingKitten= "Tacocat"

print(f'es {explodingKitten=} un palindromo? {esPalindromo(explodingKitten)}')

'''
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.
'''

def fizzBuzz ():
  i=1
  while i <51:
    if (i % 3)==0 and (i%5)==0 :
      print("FizzBuzz")
    elif (i%3)==0:
      print("Fizz")
    elif (i%5)==0:
      print("Buzz")
    else:
      print(i)
    i+=1
fizzBuzz()

'''
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.
'''

def orderList(lista):
  try:
    lista.sort(reverse=False) 
    return lista
  except TypeError:
    print("Esta lista tiene cosas no comparables, probaste con hacerlo o todo integros o todo texto? ")

print("ordenar una lista cualquiera")
print(lista_cualquiera)
print(orderList(lista_cualquiera))
print("solo un tipo")
print(lista_cualquiera_2)
print(orderList(lista_cualquiera_2))
lista_cualquiera_str = ["b", "a", "gato", "abeja", "perro", "pajaro", "esternocleidomastoideo"]
print(lista_cualquiera_str)
print(orderList(lista_cualquiera_str))

'''
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
'''
def findLongWords (list, n):
  longWords = []
  for element in list:
    wordLength = len(str(element))
    if wordLength > n:
      longWords.append(element)
  return longWords
lista_de_palabras_largas = findLongWords(lista_cualquiera_str, 3)
print(lista_de_palabras_largas)

'''
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
'''

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

'''
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
'''
def check_list_only_numbers(list):
  # check if all elements in ls are integers https://datascienceparichay.com/article/python-check-list-contains-only-numbers/
  return all([isinstance(item, int) for item in list])
print(check_list_only_numbers(lista_cualquiera_2))

def get_highest_num(lista):
  if check_list_only_numbers(lista):
    return max(lista)
  else:
    print("Necesito solo números")

print(get_highest_num(lista_cualquiera_2))
'''
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
'''
# #Si fuese lista
# def sumatorio_de_cubos(lista):
#   if check_list_only_numbers(lista):
#     sum = 0
#     for num in lista:
#       sum = num**3+sum
#     return sum
#   else:
#     print("Necesito solo números")

# print(sumatorio_de_cubos(lista_cualquiera_2))
# print(sumatorio_de_cubos([2,2]))

  
def sumatorio_de_cubos_digitos(n):
  if isinstance(n, int):
    sumatorio_de_cubos=0
    for elem in str(n):
      sumatorio_de_cubos= sumatorio_de_cubos+int(elem)**3
    return sumatorio_de_cubos

print(sumatorio_de_cubos_digitos(54))

'''
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
'''

def get_second_highest_num(lista):
  if check_list_only_numbers(lista):
    deDuped = list(set(lista))
    deDuped.remove(max(deDuped))
    return max(deDuped)
  else:
    print("Necesito solo números")
print(lista_cualquiera_2)
print(get_second_highest_num(lista_cualquiera_2))

'''
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
'''
  

def any_common (lista1, lista2):
  for elem in lista1:
    if lista2.count(elem) >0:
      return True
      break
    
  return False

print(any_common(lista_cualquiera, lista_cualquiera_2))
print(any_common(lista_cualquiera, lista_cualquiera_str))