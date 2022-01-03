# algoritmo que receba a idade de uma pessoa e informe se ela é obrigada ou não a votar, ou então se seu voto é facultativo.

def votar(age: int) -> str:
    if age >= 18:
        return print("Voto é obrigatorio")
    elif age >= 16 and age < 18:
        return print("Voto é facultativo")
    else:
        return print("Voto não obrigatório")

votar(int(input("Sua idade:")))