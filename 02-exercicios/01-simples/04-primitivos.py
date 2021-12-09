"""
LEIA QUALQUER COISA E MOSTRE O MAXIMO DE FUNÇÃO PARA UMA STRING
"""
x = input('Digite algo: ')

# funcao .is
print('Tipo primitivo: {}'.format(type(x)))
print('É numero:', x.isnumeric())
print('É alfabético:', x.isalpha())
print('É alfanúmero:', x.isalnum())
print('Está em maiusculo:', x.isupper())
print('Está em minusculo:', x.islower())
