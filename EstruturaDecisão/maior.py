'''
1. Faça um Programa que peça dois números e imprima o maior deles
'''

num1 = int(input('Informe um número: '))
num2 =int(input('Informe outro número: '))
maior = 0
if num1 > num2:
  maior = num1
else:
  maior = num2
print(f'O maior número é {maior}')
