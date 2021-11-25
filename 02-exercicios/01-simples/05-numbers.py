from math import *
# sucessor e antecessor de um numero 
num = int(input('Enter a number: '))
print('Antecessor de {} = {}\n Sucessor de {} = {}'.format(num, (num-1), num, (num+1)))

# Doblo, triplo e raiz quadrada
print('Doblo de {} = {}\n Tiplo de {} = {}\n Raiz Quadrada de {} = {:.2f}'.format(num,(num*2),num,(num*3),num, sqrt(num)))