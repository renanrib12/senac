n1 = input("Digite o primeiro nome: ")
n2 = input('Digite o segundo nome: ')
n1 = n1.lower()
n2 = n2.lower()
if (n1 == 'senac' or n2 == 'cinelandia'):
    print(f'Bem vindo, {n1} {n2}')
else:
    print('Você não é senac')