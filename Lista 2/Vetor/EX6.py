# Leia dois vetores de 6 posições e calcule um terceiro vetor contendo, nas posições
# pares os valores do primeiro e nas posições impares os valores do segundo.

vetor1 = [1, 2, 3, 4, 5 ,6, 7, 8]
vetor2 = [7, 8, 9, 10, 11, 12, 13, 14, 15]
vetor3 = []

for valor in range(len(vetor1)):
    if valor % 2 == 0:
        vetor3.append(vetor1[valor])

for valor in range(len(vetor2)):
    if valor % 2 != 0:
        vetor3.append(vetor2[valor])

print(vetor3)