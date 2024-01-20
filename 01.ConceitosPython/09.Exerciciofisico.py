""" Instruções: Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício. """

print("----- Queima caloria -----")

horasemana = float(input("Informe quantas horas você treina por semana: "))
horadia = horasemana/7
horames = horadia * 30
minutos = horames * 60

calorias = (minutos*5) 

print(f"Você gasta {calorias:.0f} calorias por mês!")