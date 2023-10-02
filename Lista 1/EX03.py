# Imprima os fatoriais de 1 a 10. O fatorial de um número n é n * (n-1) * (n-2) * ... * 1.

for numero in range(1, 11):
    total = numero * (numero - 1)
    print(total)
