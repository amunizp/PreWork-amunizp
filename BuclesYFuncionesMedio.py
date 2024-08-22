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

'''
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
'''
def reverseList (ls):
  return ls[::-1]
print(lista_cualquiera_str)
print(reverseList(lista_cualquiera_str))
'''
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
'''
def count_int_str (ls):
  num_letters=0
  num_ints=0
  for element in ls:
    if element.isdigit():
      num_ints = num_ints+1
    elif element.isalpha():
      num_letters = num_letters+1
  return num_ints, num_letters

random_string= "Ran678óm ^*ñ"
print(f'Number of numbers and letters   in a {random_string} string {count_int_str(random_string)}')

'''
22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
'''
#esto parece una version simplificada de algo que ya hice?

def sumaLista(int_ls):
  laSuma=0
  for n in int_ls:
    laSuma = laSuma + n
  return laSuma


print(sumaLista(lista_cualquiera_2))

'''
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
'''
#max(set(ls), key=ls.count) falla en test que pasa si todas son únicas? o hay dos de cada? Que pasa si no hay uno más commun que otro?
# no puedo ayudarme de un dicctionario poque la lista puede contener otras listas o diccionarios y eso no lo puedo poner de key.
#No puedo ayudarme de Set por lo mismo.
# normalmente usaría un import math or scipy de algún tipo. 

def deDuplicateList(duplicated_list):
  deduplicated_list = []
  for item in duplicated_list:
    if item not in deduplicated_list:
        deduplicated_list.append(item)
  return deduplicated_list
def most_common_in_list(lst):
  countList   = []
  noDupes = deDuplicateList(lst)
  for item in noDupes:
     countList.append( lst.count(item))
  #print(noDupes)
  #print(countList)
  indexOfMax=[]
  maxnumber = max(countList)
  j=0
  for elem in countList:
    if elem == maxnumber:
      indexOfMax.append(j)
    j+=1
  if len(indexOfMax)==1:
    #print(f'{indexOfMax=}, {maxnumber}')
    return noDupes[indexOfMax[0]]
  else:
    return "Hay más de un elemento más común"

lista_cualquiera_rara = [[0], {'gato':3,'perro':"chilla"}, 3, 4, lista_cualquiera, 4]
print("ejercicio 23 elemento mas comun de una lista")
print(lista_cualquiera)
print(most_common_in_list(lista_cualquiera))
print(lista_cualquiera_2)
print(most_common_in_list(lista_cualquiera_2))
print(lista_cualquiera_str)
print(most_common_in_list(lista_cualquiera_str))
print(lista_cualquiera_rara)
print(most_common_in_list(lista_cualquiera_rara))

'''
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
'''

def tablaMultiplicar(n):
  return {x: x*n for x in range(1,11)}

print(tablaMultiplicar(5))
diccionarioTabla7 =tablaMultiplicar(7)

'''
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
'''
def stringFrequency(chain):
  frequency ={}
  
  for elem in deDuplicateList(list(chain)):
    frequency[elem] = chain.count(elem)
  return frequency

print(stringFrequency(random_string))
random_string_2 = "22222288889asdfasdfasdf"
print(stringFrequency(random_string_2))

'''
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
'''


def nonCommonFromLists(lst1, lst2):
  list2No1=[elem for elem in lst2 if elem not in lst1]
  list1No2 =[elem for elem in lst1 if elem not in lst2]
  return list2No1+list1No2

print(f'lo que no tiene en commun {lista_cualquiera=} y {lista_cualquiera_2=} es {nonCommonFromLists(lista_cualquiera, lista_cualquiera_2)}')
print(f'lo que no tiene en commun es {nonCommonFromLists([1,2], [3, 4])}')

'''
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
'''
#ya lo habia hecho de muleta arriba cuando set y dictionary me fallaron 
duplicated_list = [1,2,1,2,2,2,3]
print(deDuplicateList(duplicated_list))
#otra manera que me quedó rara:
def deDuplicateList2(duplicated_list):
  singularity =[]
  [singularity.append(item) for item in duplicated_list if item not in singularity] #none none none
  return singularity
print(deDuplicateList2(duplicated_list))

#print(singularity2)
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

print(add_squares_of_even(5))

'''
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
'''

def average_of_list (lst):
  return sum(lst)/len(lst)


lista_cualquiera_num = [1,2,1,-2,2,2.4,3]
print(average_of_list(lista_cualquiera_num))
print(average_of_list([1,2,3]))

'''
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
'''
def findLongWords (lst):
  firstLongestWord=max(lst, key=len)
  lst.remove(firstLongestWord)
  secondLongestWord=max(lst, key=len)
  if len(firstLongestWord)==len(secondLongestWord):
    print("there are at least two longest words I will give you the first one")
  return firstLongestWord

print("longest word in the list ", findLongWords(lista_cualquiera_str))
print("longest word in the list ", findLongWords(["gato", "perro", "perra"]))

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
print(lista_de_primeros_primos(5))

'''
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''
def reverse_words (str):
  word_list = str.split()
  sentence=''
  for item in word_list:
    sentence = sentence + ' '+ item[::-1]


  return sentence.strip()

cadena_cualquiera = "Fray perico y su burrico."
print(reverse_words(cadena_cualquiera))

'''
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
listaDeTuplas = [(1, 2), (3, 4, 5), (6, 7), (8, 9, 10, 11), (12, 13), (14, 15, 16)]
listaDeTuplas2= [(14, 73), (28, 42, 91), (19, 67), (85, 31, 46, 98), (22, 13), (49, 81, 25)]
def lastElement (thetuple):
  print(thetuple[-1])
  return thetuple[-1]
def tidyListOfTuples (lstofTuples):
  lstofTuples.sort(key=lastElement)
  return lstofTuples

print(tidyListOfTuples(listaDeTuplas2))
    
'''
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''
#esto es igual que el número 5?

'''
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
'''
#hecho como part de ejercicio 31. 
print("son primos?")
print("67 ",esPrimo(67))
print("4 ", esPrimo(4))
print("9 ", esPrimo(4))