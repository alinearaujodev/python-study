# entre com seu peso, e escolha entre ver qual opcao quer saber kg ou pound
 
weight = int(input('Qual seu peso: '))
option = input('(k)g ou (L)bs: ')

if option == 'l' or 'L':
    count = weight * 0.45
    print(f'Weight in Lbs: {count}')
elif option == 'k' or 'K':
    count = weight / 0.45
    print(f'Weight in Kg: {count}')

