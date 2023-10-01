# Declare um vetor de 10 posições e o preencha somente com números impares que
# o usuário informar, e apresente o vetor.

vetor = []

for numero in range(1, 11):
    vetor.append(int(input('Digite apenas numeros impares: ')))

print(vetor)
