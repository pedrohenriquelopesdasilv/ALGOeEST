num1= int(input("insira o primeiro numero"))
num2= int(input("insira o segundo numero"))
opcao=input("insira a operação desejada(soma,subtracao,divisao,multiplicacao)")
soma=num1+num2
sub=num1-num2
div=num1/num2
mult=num1*num2
if opcao == "soma":
    print(soma)
if opcao == "subtracao":
    print(sub)
if opcao == "divisao":
    print(div)
if opcao == "multiplicacao":
    print(mult)
else :
    print("operacao invalida")