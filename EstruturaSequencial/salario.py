'''
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

valor_hora = float(input('Informe o valor por hora: R$ '))
horas_trab = int(input('Quantidade de horas trabalhadas no mês: '))
salario = valor_hora * horas_trab
print(f'O valor do salário é R$ {salario:.2f}')
