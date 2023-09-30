# Escreva um programa em Python que leia uma opção do usuário (1, 2 ou 3) e
# execute uma das seguintes ações:
# Imprima "Opção 1 escolhida"
# Imprima "Opção 2 escolhida"
# Imprima "Opção 3 escolhida"
# Se a opção escolhida pelo usuário não for válida, imprima "Opção inválida".

print('Escolha uma das 3 opções')
print('Opção 1')
print('Opção 2')
print('Opção 3')
opcao = int(input('digite o numero da opção: '))

if opcao == 1:
    print('Opção 1 escolhida')

elif opcao == 2:
    print('Opção 2 escolhida')

elif opcao == 3:
    print('Opção 3 escolhida')

else:
    print('Opção não existe')