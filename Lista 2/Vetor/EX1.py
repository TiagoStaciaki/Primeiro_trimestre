# Leia um vetor de 12 posições e em seguida ler também dois valores X e Y
# quaisquer correspondentes a duas posições no vetor. Ao final seu programa
# deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

x = int(input('Digite uma posição: '))
y = int(input('Digite outra posição: '))

resultado = vetor[x - 1] + vetor[y - 1]

print(resultado)