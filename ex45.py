#%%
def num(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return ('São iguais')
n1=float(input('Digite um valor: '))
n2=float(input('Digite outro valor: '))
maior=num(n1,n2)
print(f'{maior}')
# %%
