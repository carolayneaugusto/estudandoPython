'''
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = str(input('Informe o seu sexo [F/M]: ')).upper()

if sexo == 'F':
  print('Feminino')
elif sexo == 'M':
  print('Masculino')
else:
  print('Sexo Inválido')
  