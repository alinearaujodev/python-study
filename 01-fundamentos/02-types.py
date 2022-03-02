# TIPOS PRIMITIVO
a = 1               # int positivo 
b = -4              # int negativo
c = 0.9             # float positivo
d = -8942.0         # float negativo

e = True            # bool True
f = False           # bool False

g = 'Olá mundo!'    # string 
h = '7.4'           # string numerica
i = ''              # string vazia

# CASO NÃO DEFINA O VALOR DA VARIAVEL, GERA UM ERRO 

# PRINTS COM VARIAVEIS 
print('O valor de A:', a)                                   # Modo 1: string, int = OKAY
print('O valor de D: {} e valor de G: {}'.format(d,g))      # Modo 2: .format será sub nas chaves
print (f'O valor de de E: {e}')                             # Modo 3: f de format                   
print('Tipo primitivo de E {}'.format(type(e)));            # saber tipo da variavel


# ERROS DE TIPOS
number = input("Enter your favorite number: ")
print(number + ' is my favorite number')            # Frase toda é uma string
age = input("Enter your age: ")
print("Your birth year: ", 2022 - int(age))         # Sem a conversão de tipo haverá um erro

# int() 
# float()
# str()
# bool()