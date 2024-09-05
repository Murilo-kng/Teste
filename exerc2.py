def fibonacci(n):
    # Inicializa os dois primeiros números da sequência
    a, b = 0, 1

    # Gera a sequência de Fibonacci até que o próximo número seja maior que o número a ser verificado
    while a <= n:
        if a == n:  # Verifica se o número atual é igual ao número a ser verificado
            return True
        a, b = b, a + b  # Atualiza os valores de a e b

    return False


# Solicita ao usuário um número para verificar se está na sequência de Fibonacci
checar = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

# Verifica e exibe o resultado
if fibonacci(checar):
    print(f"O número {checar} está na sequência de Fibonacci.")
else:
    print(f"O número {checar} NÃO está na sequência de Fibonacci.")
