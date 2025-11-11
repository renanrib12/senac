t=int(input("Digite a temperatura atual: "))
if t <= 18:
    print('Está frio.')
elif 18 < t <= 30:
    print('Está agradável.')
else:
    print('Está calor.')