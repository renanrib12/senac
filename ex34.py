#%%
senha='python123'
tents=0
max_tent=3
while tents<max_tent:
    tent=input(f'Digite a senha (tentativa {tents + 1} de {max_tent})')
    if tent == senha:
        print('Acesso concedido. Bem-vindo.')
        break
    else:
        print('Senha Incorreta.')
        tents += 1
else:
    print ('Voce excedeu o úmero máximo de tentativas. Acesso bloqueado.')
# %%
