# Aluguel de carro
'''
1km = R$0.15
1d = R$60,00
'''
dias = int(float(input('Quantos dias alugados? ')))
km = float(input('Quantos Km rodados? '))

preco_dia = (dias * 60)
preco_km  = (km * 0.15)
pago = preco_dia + preco_km

print('O total a pagar é de R${:.2f}'.format(pago))