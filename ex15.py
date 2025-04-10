nomedoproduto=input("insira o nome do produto")
quantidade=int(input("qual foi a quantidade"))
preco=input("qual o preço da produto?")
total=quantidade*preco
desconto=total*0.05
if total>=100:
        print(f"compra com desconto de 5%{total-desconto}")
else:
        print("compra sem desconto")