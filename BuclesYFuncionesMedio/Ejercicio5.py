'''
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''

def cuentaVocales(cadena):
  vocales = ['a', 'e', 'i', 'o' , 'u']
  stringAsList = list(cadena.lower())
  i = 0 
  for vowel in vocales:
    i = i + stringAsList.count(vowel)
  return i

def main():
  frase = "perro de lucas"
  number = cuentaVocales(frase)
  print(f"{frase=} tiene este numero {number} de vocales")
  
  OtraFrase = input("Give me a phrase and I will count the number of vowels: ")
  print(f"{cuentaVocales(OtraFrase)} vocals.")

if __name__ == '__main__':
    main()