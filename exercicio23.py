numero = []
numero = int(input("digite um numero inteiro: "))
tabuada = []
for i in range(1,11):
    resultado = numero * i
    tabuada.append(resultado)
    print("Tabuada do {numero}:")
    for i in range(10):
        print(f"{numero} x {i + 1} = {tabuada}")