base =  int(input("Insira o numero desejado: "))
inicio =  int(input("Insira o inicio desejado: "))
fim =  int(input("Insira o fim desejado: "))
def tabuada_personalizada(base, inicio, fim):
     print(f"Tabuada do {base} de {inicio} a {fim}: ")
     for j in range(inicio, fim + 1):
         print(f"{base} x {j} = {base * j}")
        
#Uso
tabuada_personalizada(base, inicio, fim)