'''
Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.

'''
a, b, c, d, e, f  = 1, -1, 2, 3, 5, 5
if a > 0:
  print("es positivo")
elif a<0:
  print("es negativo")
else:
  print("no es ni negativo ni positivo")
 
if (d % 2) >0:
  print("Es impar")
else:
  print("es par")
# modo directo
print(max(d, e, f))
# con dondicionales
if a >= b and a >= c:
  print("El mas grande es ", a)
elif b >= a and b >= c:
  print("el mas grande es ", b) 
elif c>= a and c >=b:
  print("el más grande es ", c)
else:
  print("el condicional ha fallado")