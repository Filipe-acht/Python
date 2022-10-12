#Aplicando descontos
preco = float(input('Preço do produto: R$ '))
novo_preco = preco - (preco * 5 / 100)

print('Preço do produto R${} com 5% de desconto, fica R${}'.format(preco, novo_preco))
