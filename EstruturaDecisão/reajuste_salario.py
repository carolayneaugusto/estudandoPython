'''
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: \
* salários até R$ 280,00, incluindo: aumento de 20%;

* salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
* salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
* salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
** o salário antes do reajuste;
** o percentual de aumento aplicado;
** o valor do aumento;
** o novo salário, após o aumento.
'''

# Recebendo o valor do salário atual
salario_atual = float(input('Informe o valor do seu salário atual: R$ '))
novo_salario = 0

print(f'O salário anterior era R$ {salario_atual:.2f}')

# Calculando os reajustes
if salario_atual < 280:
  novo_salario = salario_atual + (20/100 * salario_atual)
  print('O percentual de aumento aplicado foi 20%')
elif 280 <= salario_atual < 700:
   novo_salario = salario_atual + (15/100 * salario_atual)
   print('O percentual de aumento aplicado foi 15%')
elif 700 <= salario_atual < 1500:
   novo_salario = salario_atual + (10/100 * salario_atual)
   print('O percentual de aumento aplicado foi 10%')
elif salario_atual >= 1500:
   novo_salario = salario_atual + (5/100 * salario_atual)
   print('O percentual de aumento aplicado foi 5%')
print(f'O novo salário é R$ {novo_salario:.2f}')
