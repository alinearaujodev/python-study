# FATIAMENTO DA STRING
frase = 'Aline de Araújo Diniz'
print(frase[13])
print(frase[9:20])              # da posição 16 até 20, mas não inclue a ultima posição
print(frase[9:21:2])                        # todas as posições, pulando de 2 em 2
print(frase[:5])                            # começo da string ate a posição indicada
print(frase[15:])                           # posição indicado até o final da string
print(frase[9::3]) # pega do numero indicado ate o final pulando de 3 em 3

# ANALISE
print(len(frase)) # retorna a quantidade de caracter total
print(frase.index('i')) # retorna a posição do caracter 
print(frase.count('i')) # quantas vezes aparece o carater na string
print(frase.find('niz')) # indica em qual posição encontrou o primeiro caracter 
print(frase.find('Heloísa')) # caso não exista retorna -1
print('Aline' in frase) # verifica se 'aline' está na string e retorna um bool 

# TRANSFORMAÇÃO
print(frase.replace('Diniz', 'Alves')) # troca de carater
print(frase.upper()) # caracter maiusculo
print(frase.lower()) # caracter minusculo    
print(frase.swapcase()) # caracter em minusculo para maiusculo e virse versa
print(frase.capitalize()) # primeiro caracter em maiusculo 
print(frase.title()) # primeiro caracter em maiusculo de cada palavra
print(frase.strip()) # remove os espaços inuteis

#  DIVISÃO
print(frase.split()) # dividir as palavras da string em uma lista 
print(frase.split()[2][3]) # além de dividir, retorna a segunda da lista e seu terceiro caracter

# JUNÇÃO
print('-'.join(frase))