compra = int(input("insira o valor da sua compra"))
desconto10 = compra=compra*0.1
desconto20 = compra=compra*0.20
desconto25 = compra=compra*0.25
if compra >= 100:
    print(desconto10)
elif compra >=500:
    print(desconto20)
elif compra >=1000:
    print(desconto25)
else:
    print(compra)
