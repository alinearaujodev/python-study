"""
Funções para uma string

Leia uma string e retorne o maximo de função
"""
x = input('Digite algo: ')

# funcao .is
print(f'Tipo primitivo: {type(x)}')
print('É numero:', x.isnumeric())
print('É alfabético:', x.isalpha())
print('É alfanúmero:', x.isalnum())
print('Está em maiusculo:', x.isupper())
print('Está em minusculo:', x.islower())
