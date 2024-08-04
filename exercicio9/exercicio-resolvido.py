"""

9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.

"""

horas_exercitadas_semana = float(input("Insira o número de horas de exercicios fisicos por semana: "))
minutos_exercitados_semana = horas_exercitadas_semana*60
calorias_queimadas_semana = 5*minutos_exercitados_semana
calorias_queimadas_mes = 4 * calorias_queimadas_semana
print(f"Número de calorias queimadas por mês: {calorias_queimadas_mes:.2f}")
