'''
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

lado = float(input('Informe o valor da medida do lado do quadrado em cm: '))
area = lado ** 2
dobro_area = 2 * area
print(f'O dobro da área dessa quadrado é {dobro_area:.1f} cm².')
