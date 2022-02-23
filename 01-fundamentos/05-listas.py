# listas são estruturas de dados, pode ser escrita como uma lista de objetos (itens) separados por vírgula, entre colchetes.
# listas são mutáveis, caso adicione um valor, poder ser alterado depois. 
# além que podem ser de diferente tipos


familia = ["aline", "heloísa", "joyce", "fábio", "adriana"]
print(familia)                      # Printando lista Familia (str)
familia[3] = "Jean"                 # Trocando a posição 3 por "Jean"
print(familia)                      # Printando família com troca

aniversario = [15, 1, 26, 7, 10]   # lista aniversario (numbers)
pessoa = ["aline", 15, True]        # lista pessoa (multiplo)

# FUNÇÕES PARA LISTAS
familia.append("allisson")          # add um novo elemento na lista
print(familia)
aniversario.insert(5, 6)            # add elemento na posição escolhida
print(aniversario)
familia.remove("allisson")          # removendo um elemento da lista
print(familia)
aniversario.sort()                  # lista em ordem (numerica ou alfabetica)
aniversario.reverse()               # colocando a lista inverso

x = [pessoa, aniversario]
#familia.extend(aniversario)         # JUNTAR LISTAS
print (familia)    

# print(familia)
print(aniversario)
aniversario.clear()
print(x)
print(len(pessoa))