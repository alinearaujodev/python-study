# algoritmo que receba um número inteiro e informe se ele é par ou ímpar.


def par_impar(num: int) -> str: 
    if num % 2 == 0:
        return print("Número par")
    else:
        return print("Número Impar")

par_impar(int(input("Enter a number: ")))
