# Escreva um programa que leia dois números inteiros e informe se pelo menos um
# deles é par.

numero1 = int(input('DIgite o primeiro numero: '))
numero2 = int(input('DIgite o segundo numero: '))

if numero1 % 2 == 0 or numero2 % 2 == 0:
    print('Pelo menos um deles é par')

else:
    print('Nenhum numero é par')