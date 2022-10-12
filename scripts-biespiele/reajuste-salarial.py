#Reajuste Salarial
salario = float(input('Qual é o salário do funcionário: R$'))
reajuste = salario + (salario * 15 / 100)

print('O salário do funcionário era R${:.2f}, com 15% de aumento R${:.2f}'.format(salario, reajuste))
