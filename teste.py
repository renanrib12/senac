1# produtos
print('Seja bemvindo: ')
print('Produtos: mouse - 10 reais')
print('Produtos: teclado - 20 reais')
print('Produtos: memória - 100 reais')
mou = 10
tec = 20
mem = 100
2#
while True:
    item = input('Qual produto deseja comprar?').lower()
    if item == ('mouse'):
        p = mou
        break
    elif item == ('teclado'):
        p = tec
        break
    elif item == ('memória') or ('memoria'):
        p = mem
        break
    else:
        print('Item inválido, tente novamente.')

3# Quantidade
qtd = int(input('Qual quantidade deseja comprar?'))

vb = p*qtd

if qtd >= 10:
    vf = vb+vb*0.10
else:
    vf = vb+vb*0.05
print(f'O valor final da compra de {qtd} {item} é {vf} reais.')