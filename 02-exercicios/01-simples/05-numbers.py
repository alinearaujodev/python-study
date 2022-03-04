from math import *

"""
Dado um numero, calcular seu sucessor, antecessor, doblo, tiplo e sua raiz quadrada
"""

num = int(input('Enter a number: '))
print(f'Antecessor: {num-1}')
print(f'Sucessor: {num+1}')
print(f'Doblo: {num*2}')
print(f'Tiplo: {num*3}')
print(f'Raiz Quadrada: {sqrt(num):.2f}') 