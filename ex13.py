v1=(float(input('Digite o primeiro número: ')))
v2=(float(input('Digite o segundo número: ')))
v3=(float(input('Digite o terceiro número: ')))

if v1 > v2 and v1 > v3:
    print(f'{v1} é maior que {v2} e {v3}.')
elif v2 > v1 and v2 > v3:
    print(f'{v2} é maior que {v1} e {v3}.')
else:
    print(f'{v3} é maior que {v1} e {v2}.')
