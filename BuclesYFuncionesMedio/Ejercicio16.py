'''
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
'''
import var
def check_list_only_numbers(list):
  # check if all elements in ls are integers https://datascienceparichay.com/article/python-check-list-contains-only-numbers/
  return all([isinstance(item, (int, float)) for item in list])
print(check_list_only_numbers(var.lista_cualquiera_2))

def get_highest_num(lista):
  lista = list(map(float, lista))
  if check_list_only_numbers(lista):
    return max(lista)
  else:
    print("Necesito solo números")

def main():
  print(get_highest_num(var.lista_cualquiera_2))
  ls = input("Give me a list of numbers and I will give you the biggest one ").split(',')
  print(ls)
  print(get_highest_num(ls))

if __name__ == '__main__':
    main()