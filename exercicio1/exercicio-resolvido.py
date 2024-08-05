# 1 - Desafio: exercicio 1


# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza as operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 != 0 else "Divisão por zero não permitida"

# Exibe os resultados
print(f"A soma de {numero1} e {numero2} é: {soma}")
print(f"A subtração de {numero1} por {numero2} é: {subtracao}")
print(f"A multiplicação de {numero1} e {numero2} é: {multiplicacao}")
print(f"A divisão de {numero1} por {numero2} é: {divisao}")
