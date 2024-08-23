'''
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.

'''
def sumaDigitos(stringNumber):
  numbersAsLetters = str(stringNumber)
  laSuma=0
  for char in numbersAsLetters:
    if char.isdigit():
      laSuma = laSuma + int(char)
  return laSuma

digitosSumados = sumaDigitos(345)
print(digitosSumados)

digitos = float(input("give me a number and I will separate it into digits and add them: "))

digitosSumados = sumaDigitos(digitos)

print(digitosSumados)
