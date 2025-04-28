numeros = []
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
    maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
        print(f"Maior número: {maior}")
print(f"Menor número: {menor}")