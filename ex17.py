
#%%
s1=1500
s2=2400
s3=4000
sf1 = s1-s1*0.12-s1*0.08
sf2 = s2-s2*0.12-s2*0.14
sf3 = s3-s3*0.12-s3*0.14
cargo = input('Digite seu cargo: ').lower()
if cargo == 'caixa':
    print('Seu salário final é: ', sf1)
elif cargo == 'vendedor':
    print(f'Seu salário final é: ',sf2)
elif cargo == 'gerente':
    print(f'Seu salário final é: ',sf3)
else:
    print('Cargo inválido.')
# %%

