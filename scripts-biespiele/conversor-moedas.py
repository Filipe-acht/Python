#Conversão de moeda:
real = float(input('Quanto de dinheiro vc tem? R$ '))

vlr_dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, vlr_dolar))