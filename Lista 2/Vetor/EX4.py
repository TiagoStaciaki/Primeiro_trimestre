# Leia um vetor de 10 posições e em seguida um valor X qualquer. Seu programa
# devera fazer uma busca do valor de X no vetor lido e informar a posição em que
# foi encontrado ou se não foi encontrado.

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = int(input('Digite um valor: '))

print(vetor.index(x))