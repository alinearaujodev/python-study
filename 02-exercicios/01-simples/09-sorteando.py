import random

# SORTEANDO UM NOME
name1 = input('Primeiro nome: ')
name2 = input('Segundo nome: ')
name3 = input('Terceiro nome: ')
name4 = input('Quarto nome: ')

lista = [name1, name2, name3, name4] # lista em python

print('Aluno escolhido:', random.choice(lista))   

# SORTEANDO UMA ORDEM
random.shuffle(lista)
print(lista)