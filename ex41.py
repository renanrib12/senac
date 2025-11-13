#%%
def somar(a,b):
    return a+b
def divi(a,b):
    if b == 0:
        print('Pecado')
    else:
        return a / b
def subt(a,b):
    return a-b
def mult(a,b):
    return a*b
escolha = ''
while escolha != '0':
    escolha=input('Digite uma opção: 1-somar, 2-subtrair, 3-multiplicar, 4-dividir. Digite 0 para parar')
    n1=float(input('n1'))
    n2=float(input('n2'))
    if escolha == '1':
        x=somar(n1,n2)
    elif escolha == '2':
        x=subt(n1,n2)
    elif escolha == '3:':
        x=mult(n1,n2)
    else:
        x=divi(n1,n2)
print(f'Resultado: {x}')
# %%
