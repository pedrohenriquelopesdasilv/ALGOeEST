email_certo = input("insira seu email")
email_certo= str.lower(email_certo)
senha=input("insira uma senha")
if len (senha)<8:
    print("sua senha deve ter mais de 8 caracteres")
else:
   senha_certa=senha
   email=input("insira o email")
   senha = input("insira a senha")   
   if email==email_certo:
       if senha==senha_certa:
           print("email e senha corretos")
           print("bem vindo ao sistema")
