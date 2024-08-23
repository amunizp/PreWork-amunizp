'''
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
'''
from Ejercicio1 import comprobar_entero_positivo



def devuelve_numero_binario(numero):
  n = comprobar_entero_positivo(numero)
  n_Binario = format(n, "b")
  return n_Binario
  
numeroCualquiera=6
print(f'El  {numeroCualquiera=} en binario es {devuelve_numero_binario(numeroCualquiera)}')

numeroCualquiera =int(input("Give me a full positive number and I will give you the binary or it. "))

print(f'El  {numeroCualquiera=} en binario es {devuelve_numero_binario(numeroCualquiera)}')
