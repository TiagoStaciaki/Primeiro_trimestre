# Leia uma matriz 3 x 3 e escreva a localização (linha e a coluna) do maior valor

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maior_numero = matriz[0][0]

for numeros in matriz:
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero

print(maior_numero)