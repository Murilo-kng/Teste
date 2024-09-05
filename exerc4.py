def representacao(estados):
    total = sum(estados.values())

    # Verifica se o total é zero para evitar divisão por zero
    if total == 0:
        return {chave: 0 for chave in estados}

    # Calcula a porcentagem de cada valor
    porcentagens = {chave: (valor / total) * 100 for chave, valor in estados.items()}

    return porcentagens


# Valores associados às siglas dos estados
estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

porcentagens = representacao(estados)

for estado, porcentagem in porcentagens.items():
    print(f"O estado {estado} representa {porcentagem:.2f}% do total.")
