""""Instruções:
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
"""

kms = float(input("Distância da viagem em quilômetros: "))

aviao = kms/600
carro = kms/100
onibus = kms/80


print(f"De avião você levará cerca de {aviao:.2f} horas(s) para chegar, enquanto o carro levará {carro:.2f} hora(s) e o ônibus levará {onibus:.2f} hora(s) para chegar!")

