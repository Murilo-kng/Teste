faturamento = {
    'dia 1': 22174.1664,
    'dia 2': 24537.6698,
    'dia 3': 26139.6134,
    'dia 4': 0.0,
    'dia 5': 0.0,
    'dia 6': 26742.6612,
    'dia 7': 0.0,
    'dia 8': 42889.2258,
    'dia 9': 46251.174,
    'dia 10': 11191.4722,
    'dia 11': 0.0,
    'dia 12': 0.0,
    'dia 13': 3847.4823,
    'dia 14': 373.7838,
    'dia 15': 2659.7563,
    'dia 16': 48924.2448,
    'dia 17': 18419.2614,
    'dia 18': 0.0,
    'dia 19': 0.0,
    'dia 20': 35240.1826,
    'dia 21': 43829.1667,
    'dia 22': 18235.6852,
    'dia 23': 4355.0662,
    'dia 24': 13327.1025,
    'dia 25': 0.0,
    'dia 26': 0.0,
    'dia 27': 25681.8318,
    'dia 28': 1718.1221,
    'dia 29': 13220.495,
    'dia 30': 8414.61
}

dias_uteis = [valor for valor in faturamento.values() if valor > 0]
menor_fatur = float('inf')
maior_fatur = 0
dia_menor_faturamento = None
dia_maior_faturamento = None

# Percorre o dicionário para encontrar o menor valor de faturamento
for dia, valor in faturamento.items():
    if valor > 0:  # Verifica se o valor é maior que zero
        if valor < menor_fatur:
            menor_fatur = valor
            dia_menor_faturamento = dia

for dia, valor in faturamento.items():
    if valor > maior_fatur:
        maior_fatur = valor
        dia_maior_faturamento = dia

if dia_menor_faturamento is not None:
    print(f"O dia com o menor faturamento foi {dia_menor_faturamento} com R$ {menor_fatur:.2f}")

if dia_maior_faturamento is not None:
    print(f"O dia com o menor faturamento foi {dia_maior_faturamento} com R$ {maior_fatur:.2f}")

# Calcula a média dos valores válidos
if dias_uteis:
    media = sum(dias_uteis) / len(dias_uteis)
else:
    media = 0

dias_acima_media = {dia: valor for dia, valor in faturamento.items() if valor > media}

print(f"Média de faturamento: R$ {media:.2f}")

if dias_acima_media:
    print("Dias com faturamento acima da média:")
    for dia, valor in dias_acima_media.items():
        print(f"Dia {dia}: R$ {valor:.2f}")
