'''
11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def esPalindromo(cadena):
  cadena = cadena.lower()
  if cadena == cadena[::-1]:
    return True
  else:
    return False

explodingKitten= "Tacocat"

print(f'es {explodingKitten=} un palindromo? {esPalindromo(explodingKitten)}')

word = input("Give me a word and I will check if it is a palindrome ")

print(f'Is {word=} a palindrom? {esPalindromo(word)}')
