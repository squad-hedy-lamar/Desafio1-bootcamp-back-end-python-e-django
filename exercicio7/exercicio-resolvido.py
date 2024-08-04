# Exercício 7 - Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).

print('==== Cálculo de IMC ====')
peso = float(input('Digite seu peso (em kg): '))
alturaM = float(input('Digite sua altura (em metros): '))

imc = peso/(alturaM*alturaM)

print('IMC = {}'.format(imc))