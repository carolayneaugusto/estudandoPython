'''
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

area = float(input('Informe o tamanho em metros quadrados da área a ser pintada? '))
litro = area / 3
lata = math.ceil(litro / 18)
preco_tinta = lata * 80
print(area, '\n', litro, '\n', lata )
print(f'Serão necessário {lata} latas de tinta e o preço total é R$ {preco_tinta:.2f}')
