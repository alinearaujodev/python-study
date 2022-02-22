import math     # importa toda a biblioteca math
                # from math import sqrt | importa somente sqrt
import random   # importa biblioteca random para numero aleatório

# OPERADORES MATEMÁTICOS 
print(1 + 1)    # soma
print(5 - 2)    # subtração
print(7 * 4)    # multiplicação
print(10 / 5)   # divisão sempre retorna um float
print(10 // 5)  # divisão que retorna um inteiro
print(10 % 3)   # resto da divisão
print(5 ** 3)   # potência

# ATRIBUIÇÃO MULTIPLA 
a, b = 1, 3
print(a, b)
a, b = b, a+b
print(a, b)

# (X = X + 1)
a += 3
print(a)

# OPERADORES LÓGICOS
print(a > 5 and a < 10)     # Ambos verdadeiros
print(b > 5 or b < 2)       # Apenas um verdadeiro
print(not a < 5)            # Não Verdadeiro

#  FUNÇÕES NICE
print(pow(9,2))                         # potência
print(max(100, 73))                     # retorna o maior numero 
print(min(7, 28))                       # retorna o menor numero
print(round(23.67))                     # arrendonda para mais ou para menos 
print(math.floor(3.8))                  # arrendonda para menos 
print(math.ceil(3.8))                   # arrendonda para mais
print(math.sqrt(random.randint(1,10)))  # raiz quadrada 