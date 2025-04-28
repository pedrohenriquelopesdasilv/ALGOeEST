notas = []

# Coletar as notas dos 5 alunos
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

# Calcular a média
soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)

# Exibir a média
print(f"A média das notas é: {media:.2f}")