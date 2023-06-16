'''
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade_internet = float(input('Informe a velocidade de um link de internet (em Mbps): '))

tempo_download = (tamanho * 8) / velocidade_internet
tempo_minutos = tempo_download / 60

print(f'O tempo de download em minutos é {tempo_minutos:.2f}')

