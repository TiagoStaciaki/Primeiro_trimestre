# Faça um programa que calcule a média de duas notas de um aluno. Apresente a
# mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A
# mensagem "Reprovado", se a média for menor do que sete; A mensagem
# "Aprovado com Distinção", se a média for igual a dez.

nome = input('Digite o nome do aluno: ')
nota1 = float(input(f'Digite a nota primeira nota do(a) {nome}: '))
nota2 = float(input(f'Digite a nota segunda nota do(a) {nome}: '))

if (nota1 + nota2) / 2 == 10:
    print(f'{nome} foi aprovado com distinção')

elif (nota1 + nota2) / 2 >= 7:
    print(f'{nome} foi aprovado')

elif (nota1 + nota2) / 2 < 7:
    print(f'{nome} foi reprovado')