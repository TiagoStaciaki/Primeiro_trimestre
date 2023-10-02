# Escreva um programa que leia um número inteiro do usuário e informe se ele é
# positivo, negativo ou zero.

numero = int(input('Digite um numero: '))

if numero > 0:
    print('Positivo')

elif numero < 0:
    print('Negativo')

elif numero == 0:
    print('Zero')
    