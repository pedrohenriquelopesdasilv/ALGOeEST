print("Cadastre-se:")
nome=input("Insira seu nome:")
idade=int(input("Sua idade:"))
turma=input("Qual turma você pertence:")
if idade>6:
    print("Aluno cadastrado com sucesso:{nome},{idade} anos, turma {turma}.")
else:
    print("Você é novo demais pra se matricular")