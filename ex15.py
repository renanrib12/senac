#%%
ano = int(input('Digite seu ano de nascimento: '))
gen = input('Seu genero: (M/F)').upper()
idade = 2025-ano
if idade >= 18 and gen == 'M':
    print('Apto a se alistar')
else:
    print('Não apto a se alistar')
# %%
