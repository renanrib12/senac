#%%
ns=42
palpite=0
print('Tente advinhar um número secreto entre 1 e 100')
while palpite != ns:
    try:
        entrada = input('Seu palpite:')
        palpite=int(entrada)

        if palpite<ns:
            print('Muito baixo')
        elif palpite>ns:
            print('Muito alto')
        else:
            print('Você acertou')
    except ValueError:
        print('Por favor, digite apenas números inteiros')

# %%
