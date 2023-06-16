'''
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso
'''

turno = str(input('Qual o turno que você estuda? [Informe M para matutino, V para vespertino e N para noturno] ')).lower()

if turno == 'm':
  print('Bom Dia!')
elif turno == 'v':
  print('Boa Tarde!')
elif turno == 'n':
  print('Boa Noite!')
else:
  print('Valor Inválido')
