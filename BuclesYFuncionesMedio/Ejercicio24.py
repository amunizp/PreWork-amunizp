'''
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
'''

def tablaMultiplicar(n):
  return {x: round(x*n, 2) for x in range(1,11)}

print(tablaMultiplicar(5))
diccionarioTabla7 =tablaMultiplicar(7)

number = float(input("give me a number and I will give you the 1-10 times table \t"))
print(tablaMultiplicar(number)) 