'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

area = float(input('Informe o tamanho da área em metros quadrados: '))

#Calculando a quantidade litros necessários 
litros = math.ceil(area / 6)
litros_com_folga = litros * 1.1

#Quantidade de latas de 18 litros
latas = math.ceil(litros_com_folga / 18)
preco_latas = latas * 80

#Calculando a quantidade de galões
galoes = math.ceil(litros_com_folga / 3.6)
preco_galoes = galoes * 25

#Calculando a mistura de latas e galões
mistura_latas = int(litros_com_folga) // 18
resto_litro = litros_com_folga % 18
galoes_mistura = math.ceil(resto_litro / 3.6)
preco_mistura = (mistura_latas * 80) + (galoes_mistura * 25)

#Resultados
print(f'Comprando apenas com latas de tinta de 18 litros, a quantidade é {latas} por R$ {preco_latas:.2f}')
print(f'Comprando apenas com galões de 3,6 litros, a quantidade é {galoes} por R$ {preco_galoes:.2f}')
print(f'Misturando latas e galões: a quantida é {mistura_latas} latas e {galoes_mistura} galão (ões) por R$ {preco_mistura}')
