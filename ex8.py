nome = input('Qual o seu nome?')
sbnome = input('Qual o seu sobrenome?')
nome = nome.upper()
sbnome=sbnome.upper()
if nome == "SENAC" and sbnome == 'SANTA LUZIA':
    print(f'Seja bem vindo, {nome} {sbnome}')
else:
    print('Não é Senac')