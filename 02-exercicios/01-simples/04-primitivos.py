"""
LEIA QUALQUER COISA E MOSTRE O MAXIMO DE FUNÇÃO PARA UMA STRING
"""
x = input('Digite algo: ')

# funcao .
print(x.lower()) # todos caracter minusculo
print(x.upper()) # todos caracter maiusculo
print(x.swapcase()) # caracter em minusculo para maiusculo e virse versa
print(len(x)) # retorna o numero de caracter da variavel 
print(x.index('A'))
print(x.replace('Aline', 'Heloísa')) #substitui uma palavra por outra 

""" 
# funcao .is
print('Tipo primitivo: {}'.format(type(x)))
print('É numero:', x.isnumeric())
print('É alfabético:', x.isalpha())
print('É alfanúmero:', x.isalnum())
print('Está em maiusculo:', x.isupper())
print('Está em minusculo:', x.islower())
""" 