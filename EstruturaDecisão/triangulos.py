'''
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
* Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
* Triângulo Equilátero: três lados iguais;
* Triângulo Isósceles: quaisquer dois lados iguais;
* Triângulo Escaleno: três lados diferentes;
'''

a = float(input('Informe o valor do lado do triângulo: '))
b = float(input('Informe o valor do lado do triângulo: '))
c = float(input('Informe o valor do lado do triângulo: '))

if (a + b) > c:
  print('Pode ser um triângulo')
  if a == b == c:
    print('É um triângulo equilátero')
  elif (a == b != c) or (a == c != b) or (b == c != a):
    print('É um triângulo isósceles')
  elif a != b != c != a:
    print('É um triângulo escaleno')
else:
  print('Não pode ser um triângulo')
