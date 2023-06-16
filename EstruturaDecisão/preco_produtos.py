'''
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

# perguntando o preço dos produtos

produto1  = float(input('Informe o valor do 1º produto: R$ '))
produto2  = float(input('Informe o valor do 2º produto: R$ '))
produto3  = float(input('Informe o valor do 3º produto: R$ '))

# comparando o preço dos produtos
if  produto3 > produto1 < produto2:
  print('Compre o primeiro porduto.')
elif produto3 > produto2 < produto1:
  print('Compre o segundo produto.')
else:
  print('Compre o terceiro produto')
