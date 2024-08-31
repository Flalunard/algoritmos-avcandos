'''
7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
Considerar ano com 365 dias e mês com 30 dias.
'''

ano=int(input('Escreva o ano '))
mes=int(input('Escreva o mês '))
dia=int(input('EScreva o dia '))
result = (ano * 365) + (mes * 30) + dia
print('Sua idade em dias são no total de ', result)
