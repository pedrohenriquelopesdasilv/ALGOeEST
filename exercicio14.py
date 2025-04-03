nome_certo="admin"
senha_certo=1234
nome=int(input("insira um nome de usuario"))
senha=int(input("insira sua senha"))
if nome == nome_certo and senha_certo == senha:
     print("bem vindo!")
else:
     print("usuario ou senha invalidos")