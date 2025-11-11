n=0
while n >= 0 and n <= 10:
    try:
        n=int(input('Digite uma nota: '))
    except ValueError:
        print('valor inteiro')
print(f'Nota inválida registrada: {n}')
