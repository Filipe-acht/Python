from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))

# Hip² = (cat_opst² + cat_adj²)
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2) # 1/2 pra ca

print('A hipotenusa vai medir {:.2f}'.format(hi))'''