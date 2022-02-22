# listas são estruturas de dados, pode ser escrita como uma lista de valores (itens) separados por vírgula, entre colchetes.
# listas são mutáveis, caso adicione um valor, poder ser alterado depois. 
# além que podem ser de diferente tipos


familia = ["aline", "heloísa", "joyce", "fábio", "adriana"]
aniversario = [15, 1, 26, 22, 10]
pessoa = ["aline", 15, True]

# FUNÇÕES PARA LISTAS
familia.extend(aniversario) # JUNTAR LISTAS
familia.append("Allisson") # adicionar um elemento da lista
familia.insert(3, "Luis") # add elemento na posição escolhida
familia.remove("Allisson") # removendo um elemento da lista
aniversario.sort() # lista em ordem (numerica ou alfabetica)
aniversario.reverse() # colocando a lista inverso
x = [pessoa, aniversario]

print(familia)
print(aniversario)
print(x)
print(len(pessoa))