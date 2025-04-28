import random
numero_secreto = random.randint(1, 20)
palpites = {}
palpite = {}
acertou=False
while not acertou:
    palpite = int(input("Digite um palpite entre 1 a 20: "))
    palpites.append(palpite)
    
    if palpite == numero_secreto:
        print("Parabéns!!! Você acertou!")
        acertou = True
    else:
        print("Errado! Tente novamente.")
    print("Seus Palpites foram:")
    print(palpites)