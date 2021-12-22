"""
PEGUE AS 4 NOTAS DO ANO DO ALUNO, MOSTRE SUA MÉDIA E SE FOI APROVADO

"""

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

media = (n1+n2+n3+n4)/4

if media > 6:
    print('Aprovado!')
else:
    print('Reprovado!')

print('Sua média foi: {:.1f}'.format(media))