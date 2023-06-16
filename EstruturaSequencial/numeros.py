'''
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a- o produto do dobro do primeiro com metade do segundo .
b - a soma do triplo do primeiro com o terceiro.
c - o terceiro elevado ao cubo.
'''
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

print(f'a - o produto do dobro do primeiro com metade do segundo: {(num1 * 2) * (num2/2)}')
print(f'b - a soma do triplo do primeiro com o terceiro: {(num1 * 3) + num3}')
print(f'c - o terceiro elevado ao cubo: {num3 ** 3}')
