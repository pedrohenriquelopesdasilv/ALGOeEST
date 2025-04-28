#entrar no clube
idade=int(input("Insira sua idade:"))
status_de_membro=bool(input("Você é membro do clube? True-Sim, False-Não"))
membro_acom=bool(input("Está acompanhado de membro? True-Sim, False-Não"))
if idade>18:
    if status_de_membro == True:
        print("Liberado")
    elif membro_acom == True:
        print("Pague meia entrada")
    else:
        print("Entrada no valor integral")
else:
    print("Você não tem idade nescessária")