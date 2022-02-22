import math # aqui tudo de math
# from math import sqrt   #importa somente a sqrt
import random # importando biblioteca random para numero aleatório

print(1 + 1) # soma
print(5 - 2) # subtração
print(7 * 4) # multiplicação
print(10 / 5) # divisão sempre retorna um float
print(10 // 5) # divisão que retorna um inteiro
print(10 % 3) # resto da divisão
print(5 ** 3) # potência

#   ERROS DE TIPOS
fav_number = input("Enter your favorite number: ")
print(fav_number + ' is my favorite number') # aqui toda a frase será uma string e a concatenação funcionar por causa do '+'

age = input("Enter your age: ")
print("Your birth year: ", 2022 - int(age)) # aqui haverá um erro por causa de dois tipos diferente: int e str, então tem que fazer conversão de tipo: 

# int() 
# float()
# str()
# bool()

# ATRIBUIÇÃO múltipla 
a, b = 1, 3
print(a, b)
a, b = b, a+b
print(a, b)

#  FUNÇÕES NICE
print(pow(9,2)) # potência
print(max(100, 73)) # retorna o maior numero 
print(min(7, 28)) # retorna o menor numero
print(round(23.67)) # arrendonda para mais ou para menos 
print(math.floor(3.8)) # arrendonda para menos 
print(math.ceil(3.8)) # arrendonda para mais
print(math.sqrt(random.randint(1,10))) # raiz quadrada 