'''
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
'''
def count_int_str (ls):
  num_letters=0
  num_ints=0
  for element in ls:
    if element.isdigit():
      num_ints = num_ints+1
    elif element.isalpha():
      num_letters = num_letters+1
  return num_ints, num_letters

random_string= "Ran678óm ^*ñ"
print(f'Number of numbers and letters   in a {random_string} string {count_int_str(random_string)}')

chain = input("Give me me some text and numbers and I will tell you how much of each\t")
print(f'Number of numbers and letters   in a {chain} numbers {count_int_str(chain)[0]} and letters {count_int_str(chain)[1]}')
