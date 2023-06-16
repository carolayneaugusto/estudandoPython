'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

if a < c:
  a, c = c, a

if a < b:
  a, b = b, a

if b < c:
  b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')
