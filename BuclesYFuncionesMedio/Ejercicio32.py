'''
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''
import var

def reverse_words (str):
  word_list = str.split()
  sentence=''
  for item in word_list:
    sentence = sentence + ' '+ item[::-1]


  return sentence.strip()

print(reverse_words(var.cadena_cualquiera))

cadena = input("give me a sentence and I will flip around each word")
print(reverse_words(cadena))