'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dia = int(input('Digite um número de 1 a 7: '))

if 0 <= dia > 7:
  print('Valor inválido')
else:
  if dia == 1:
    print('Domingo')
  elif dia == 2:
    print('Segunda-feira')
  elif dia == 3:
    print('Terça-feira')
  elif dia == 4:
    print('Quarta-feira')
  elif dia == 5:
    print('Quinta-feira')
  elif dia == 6:
    print('Sexta-feira')
  elif dia == 7:
    print('Sábado')
    