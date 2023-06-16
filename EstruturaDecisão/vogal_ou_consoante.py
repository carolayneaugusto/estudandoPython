'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = str(input('Digite uma letra: ')).upper()

if letra in 'AEIOU':
  print('vogal')
else:
  print('consoante')
  