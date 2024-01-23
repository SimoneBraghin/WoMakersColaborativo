# Instruções
'''07.Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índicede Massa Corporal(IMC)
usando a fórmula:IMC=peso/(altura x altura).
'''
simbolo = "-"
quantidade = 15
traco = simbolo*quantidade

print(f"{traco} Cálculo IMC {traco}")
peso = float(input("Informe seu Peso em Kg : "))
altura = float(input("Informe a altura em metros:"))

imc= peso/(altura*altura)

print(f"Seu Índice de Massa Corporal é : {imc:.2f}")

print(f"{traco} Fim do Programa {traco}")