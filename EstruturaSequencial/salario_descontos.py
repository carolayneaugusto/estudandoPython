'''
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:

```
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
```

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
hora_valor = float(input('Quanto você ganha por hora? R$ '))
num_horas = int(input('Quantidade de horas trabalhadas no mês: '))
salario_bruto = hora_valor * num_horas
ir = salario_bruto * 11/100
inss =  salario_bruto * 8/100
sindicato =  salario_bruto * 5/100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print(f'Seu salário bruto foi de R$ {salario_bruto:.2f}')
print(f'Foi pago ao IR R$ {ir:.2f}'),
print(f'Foi pago ao INSS, R$ {inss:.2f}')
print(f'Foi pago ao Sindicato o total de R$ {sindicato:.2f}')
print(f'O salário liquído é R$ {salario_liquido:.2f}')
