# listas são estruturas de dados
# caso adicione um valor, poder ser alterado depois


familia = ["aline", "heloísa", "joyce", "fábio", "adriana"]
aniversario = [15, 1, 26, 22, 10]

# FUNÇÕES PARA LISTAS
familia.extend(aniversario) # JUNTAR LISTAS
familia.append("Allisson") # adicionar um elemento da lista
familia.insert(3, "Luis") # add elemento na posição escolhida
familia.remove("Allisson") # removendo um elemento da lista
aniversario.sort() # lista em ordem (numerica ou alfabetica)
aniversario.reverse() # colocando a lista inverso

print(familia)
print(aniversario)