numero = int(input("Insira o numero desejado: "))
def tabuada (numero):
    print(f"Tabuada do {numero}: ")
    for i in range (1, 11):
          print(f"{numero} x {i} = {numero * i}")

#Exibir as tabuadas
tabuada(numero)