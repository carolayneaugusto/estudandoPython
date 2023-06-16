'''
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

```
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

```
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
conceito = ''
if media > 9:
  conceito = 'A'
elif 9 >= media > 7.5:
  conceito = 'B'
elif 7.5 >= media > 6:
  conceito = 'C'
elif 6 >= media > 4:
  conceito = 'D'
else:
  conceito = 'E'

print(f'As notars foram {nota1} e {nota2}')
print(f'Sua média é {media}')
print(f'O conceito é {conceito}')

if conceito in 'ABC':
  print('APROVADO')
else:
  print('REPROVADO')

