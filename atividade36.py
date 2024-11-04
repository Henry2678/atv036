# Ler uma lista com 4 notas, em seguida
# o programa deve exibir as notas e a
#média.
# Inicializa uma lista para armazenar as notas
notas = []

# Lê 4 notas do usuário
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Calcula a média
media = sum(notas) / len(notas)

# Exibe as notas e a média
print("Notas:", notas)
print("Média:", media)
