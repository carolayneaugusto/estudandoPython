'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite o último valor: '))
maior = n1

if n2 > n1 and n2 > n3:
  maior = n2
elif n3 > n2 and n3 > n1:
  maior = n3

print('O maior é ', maior)
