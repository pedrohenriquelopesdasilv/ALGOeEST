status_da_conta= True
saldo = float(input("insira o saldo da conta"))
if saldo == 0:
    status_da_conta = False
    print("sua conta esta inativa")
elif saldo <0:
    print("renegocie sua divida")
else:
    print("sua conta esta ativa")