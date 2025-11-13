#%%
sp = 0
n=-1
while n != 0:
    entrada=input('Digite um número (0 para parar)')
    try:
        n=int(entrada)
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
        continue
    if n>0:
        sp=sp+n
print(f'A soma dos números positivos é: {sp}')
# %%

