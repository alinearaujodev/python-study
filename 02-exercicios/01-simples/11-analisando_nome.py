# leia um nome completo e sua 
nome = input('Digite seu nome completo: ')

print('Nome em Maiusculo: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
dividido = nome.split()
espaco = nome.count(' ')
print('Quantas letras tem seu nome: {}'.format(len(nome) - espaco))
print('Quantas letras tem seu primeiro nome: {}'.format(len(dividido[0])))
print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[len(dividido)-1]))
print('Quantas vezes aparece a letra a: {} e sua posição: {}'.format(nome.count('a'), nome.index('a')))