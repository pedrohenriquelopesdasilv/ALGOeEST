print("CADASTRE-SE:")
email=input("insira o e-mail desejado:")
email_certo=str.lower(email)
senha=input("Digite sua senha:")
if len(senha)>=8:
    print("Senha válida. Cadastro efetuado com sucesso")
    print("Sua conta está cadastrada, insira o login")
    login=input("Insira o email cadastrado:")
    chave=input("Insira a senha:")
    if login ==email and senha ==chave:
        print("Login efetuado com sucesso.")
    else:
        print("Login incorreto!")
else:
    print("Senha inválida")
