#%%
def somar(a,b):
    return a+b
n1=int(input('n1'))
n2=int(input('n2'))
soma=somar(n1,n2)
print(f'{soma}')
# %%
n1=int(input('n1'))
n2=int(input('n2'))
def divi(a,b):
    if b == 0:
        print('Pecado')
    else:
        return a / b
x=divi(n1,n2)
print(f'{x}')
# %%
