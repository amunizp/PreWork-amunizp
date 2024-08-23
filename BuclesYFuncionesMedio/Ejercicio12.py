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

