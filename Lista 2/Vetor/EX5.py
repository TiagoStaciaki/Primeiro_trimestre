# Leia um vetor de 15 posições. Contar e escrever quantos valores pares ele possui.

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numerosP = 0

for indicie in vetor:
    if indicie % 2 == 0:
        numerosP += 1

print(numerosP)