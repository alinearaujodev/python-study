"""
Aprovação de emprestimo bancário

:Parametro house_value: float - valor da casa
:Parametro salary: float - salario do comprador 
:parametro year: int - quantos anos o comprador vai pagar a casa
:return float - valor da prestação mensal

Calcule o valor da prestação mensal, sabendo que deverá aplicar um juros de 25% sobre o valor da casa e não pode exceder 30% do salario do comprador, ou então se negado o emprestimo
"""

house_value = float(input('Valor da casa: '))
salary = float(input('Salario do comprador: '))
year = int(input('Anos para o pagamento da casa: '))

juros = ((house_value * 25) / 100) + house_value
prestacao = juros / year

if prestacao < (salary * 30)/100:
    print('----------------------------------')
    print('Parabéns! Aprovamos seu empréstimo')
    print(f'Com prestações mensais de {prestacao:.2f}, durante {year} anos')
else:
    print('Infelizmente não conseguimos aprovar um empréstimo no momemto para você :(')

