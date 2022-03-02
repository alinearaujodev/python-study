"""
Calculadora

:parametro num1: float - numero 1 para o calculo 
:parametro op: string - operador matématico do calculo
:parametro num2: float - numero 2 para o calculo

A depender de um determinado operador matématico, fazer o calculo da operação
"""

num1 = float(input('Numero 1: '))
op = input('Operador: ')
num2 = float(input('Numero 2: '))

if op == '+':
    print('Soma:', num1 + num2)
elif op == '-':
    print('Subtração: ', num1 - num2)
elif op == '*':
    print('Multiplicação: ', num1 * num2)
elif op == '/':
    print('Divisão: ', num1 / num2)
else:
    print('Operador não existe')