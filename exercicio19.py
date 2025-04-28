#anuncio de venda categorias
idade=int(input("Insira a idade:"))
sexo=int(input("Qual seu gênero, 1-Homem 2-Mulher:"))
atleta=bool(input("Você é atleta? True-Sim, False-Não:"))
if idade<15:
    print("Artigos infantis")
elif sexo == 2 and idade<=21:
    print("Maquiagem moda")
elif idade>15 and sexo == 1 and idade<=32 and atleta == True:
    print("Artigos Esportivos")
elif idade>21 and sexo == 1 and idade<21 and atleta == False:
    print("Videogames")
elif idade>21 and sexo == 1 and idade<= 32 and atleta == False:
    print("Livros, Jardinagem e Eletrodomesticos")
elif sexo == 2 and idade<=35 and idade>22:
    print("Oferecer artigos esportivos e itens de casa")
else:
    print("Não há anuncios adequados a estas características.")