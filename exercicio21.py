numeros = []
for i in range(1,11):
    num = int(input(f"Digite o {i}° numero inteiro: "))
    numeros.append(num)
print(numeros)
for numero in numeros:
    print(numero)
    soma = 0
    for numero in num:
        soma +=numero
        print(f"Soma de todos os numeros: {soma}")