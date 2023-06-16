'''
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite o último valor: '))
menor = n1

if n3 > n2 < n1:
  menor = n2
elif n1 > n3 < n2:
  menor = n3

print('O menor é ', menor)
