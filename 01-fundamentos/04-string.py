# FATIAMENTO DA STRING
frase = 'Aline de Araújo Diniz'
print(frase[13])
print(frase[9:20]) # pega a posição 16 até 20, mas não inclue a ultima posição
print(frase[9:21:2]) # pega as posições, mas pulando de 2 em 2
print(frase[:5]) # pega o começo da string ate o numero indicado
print(frase[15:]) # pega do numero indicado até o final da string
print(frase[9::3]) # pega do numero indicado ate o final pulando de 3 em 3

# ANALISE
print(len(frase)) # retorna o numero de caracter total da string
print(frase.count('i')) # quantas vezes aparece o carater na string
print(frase.find('niz')) # indica em qual posição encontrou o primeiro caracter 
print(frase.find('Heloísa')) # caso não exista retorna -1
print('Aline' in frase) # retorna um bool 

# TRANSFORMAÇÃO
print(frase.replace('Diniz', 'Alves')) # troca de carater
print(frase.upper()) # caracter maiusculo
print(frase.lower()) # caracter minusculo    
print(frase.capitalize()) # primeiro caracter em maiusculo 
print(frase.title()) # primeiro caracter em maiusculo de cada palavra
print(frase.strip()) # remove os espaços inuteis

#  DIVISÃO
print(frase.split()) # dividir as palavras da string em uma lista 
print(frase.split()[2][3]) # além de dividir, retorna a segunda da lista e seu terceiro caracter

# JUNÇÃO
print('-'.join(frase))