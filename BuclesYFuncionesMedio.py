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