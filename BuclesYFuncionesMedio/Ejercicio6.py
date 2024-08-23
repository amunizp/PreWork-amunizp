'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
'''
def cogeLosPrimeros (list, n):
  return list[0:n+1]

n = 4
lista_cualquiera = [2, 3, 5 , 6, 7,8, 6,3, 5, 2, 1, "e", 1]
primeraparte= cogeLosPrimeros(lista_cualquiera, n)
print(primeraparte)

ls = list(input("Give me a list separated by comas: ").split(','))
n = int(input("Tell me how many of the list to you want to see: "))

print(cogeLosPrimeros(ls, n))