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
  if isinstance(n, (int,float)):
    sumatorio_de_cubos=0
    for elem in str(n):
      if elem.isdigit():
        sumatorio_de_cubos= sumatorio_de_cubos+int(elem)**3
    return sumatorio_de_cubos

print(sumatorio_de_cubos_digitos(54))
n = float(input("Give me a digital number and I will add the cube of each digit "))
print(sumatorio_de_cubos_digitos(n))