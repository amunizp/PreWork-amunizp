'''IntroduccionPython-Bucles.pdf
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.

'''
i =1
while i <=10:
  print(i)
  i+=1


j =1
while j <=20:
  if (j  % 2) == 0 :
    print(j)
  j+=1

k =1
total = 0
while k <=100:
  total = total +k
  k+=1
print(total)

 
'''
O sin bucle usando la pista del triangulo de antes
x                 o      x o o o o o
x x             o o      x x o o o o
x x x         o o o  =>  x x x o o o
x x x x     o o o o      x x x x o o
x x x x x o o o o o      x x x x x o
'''
numero = 100
sumatorio = numero *(numero+1)/2
print(sumatorio)
