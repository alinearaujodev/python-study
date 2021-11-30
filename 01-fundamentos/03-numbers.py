import math # aqui tudo de math
# from math import sqrt   #importa somente a sqrt
import random # importando biblioteca random para numero aleatório
import emoji

print(1 + 1) # soma
print(5 - 2) # subtração
print(7 * 4) # multiplicação
print(9 / 6) # divisão 
print(10 % 3) # resto da divisão

"""
Vai funcionar somente com a concatenação com o + 
porque o number ficou como uma string
Agora de tirar a função str, vai dar typeerror 

"""
my_num = 15
print(str(my_num) + ' my favorite number') 

#  FUNÇÕES NICE
print(pow(9,2)) # potência
print(max(100, 73)) # retorna o maior numero 
print(min(7, 28)) # retorna o menor numero
print(round(23.67)) # arrendonda para mais ou para menos 
print(math.floor(3.8)) # arrendonda para menos 
print(math.ceil(3.8)) # arrendonda para mais
print(math.sqrt(random.randint(1,10))) # raiz quadrada 

# EMOJI 
print(emoji.emojize('Python is :thumbs_up:'))