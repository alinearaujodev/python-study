# calcule a média de duas notas de um aluno
name = input('Nome do Aluno: ')
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))

media = (nota1+nota2)/2
print('Média de {} = {}'.format(name,media))