# Escreva um programa que leia um número inteiro do usuário e imprima se ele é
# par ou ímpar.

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print(f'o numero {numero} é par')

elif numero % 2 != 0:
    print(f'o numero {numero} é impar')