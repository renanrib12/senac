n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
n3 = float(input('Digite a nota 3:'))
n4 = float(input('Digite a nota 4:'))
media = ((n1+n2+n3+n4)/4)
if media >= 7:
    print(f'Nota: {media}. O aluno está aprovado!')
else:
    print(f'Nota: {media}. O aluno está em recuperação!')