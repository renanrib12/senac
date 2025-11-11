n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
if n2 == 0:
    print ('Impossível dividir por 0')
else:
    soma = n1/n2
    print("O resultado da soma é: ",soma)
    print(f'O resultado entre a soma {n1} e {n2} é {soma}')