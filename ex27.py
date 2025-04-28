nomes = []

# Coletar os nomes de 5 amigos
for i in range(5):
    nome = input(f"Digite o nome do amigo {i + 1}: ")
    nomes.append(nome)

# Ordenar a lista em ordem alfabética
nomes.sort()

# Exibir os nomes em ordem alfabética
print("\nNomes em ordem alfabética:")
for nome in nomes:
    print(nome)