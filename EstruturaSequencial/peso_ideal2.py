'''
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7
'''

h = float(input('Informe a sua altura: '))

homens = (72.7 * h) - 58
mulheres = (62.1 * h) - 44.7

print(f'Peso ideal para homens é {homens:.1f} kg e para mulheres é {mulheres:.1f} kg.')
