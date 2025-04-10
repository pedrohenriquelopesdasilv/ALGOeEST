nome=input("insira seu nome")
idade=int(input("isira sua idade"))
turma=input("insira sua turma")
 
if idade>=6:
     print(f"aluno cadastrado com sucesso{nome},{idade} anos,turma {turma}")
else:
     print("a criança ainda não tem idade o suficiente para estudar conosco")