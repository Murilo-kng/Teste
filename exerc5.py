palavra = input("Digite uma string para inverter: ")

# Inverte a string usando um loop for
invertida = ''
for caract in palavra:
    invertida = caract + invertida  # Adiciona cada caractere no início da nova string

print(f"A string invertida é: {invertida}")
