#%% Progressão Aritmética

a=int(input('Digite o calor de a: '))
r=int(input('Digite o valor da razão: '))
n=int(input('Digite a posição do último termo: '))
pa = []
for i in range(0,n):
    termo = (a+i*r)
    pa.append(termo)
print(pa)

# %% Progressão Geométrica

a=int(input('Digite o calor de a: '))
r=int(input('Digite o valor da razão: '))
n=int(input('Digite a posição do último termo: '))
pg = []
for i in range(0,n):
    termo = int(a*r**(i-1))
    pg.append(int(termo))
print(pg)


# %%
