# Instruções
'''8. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

simbolo = "-"
quantidade = 15
traco = simbolo*quantidade

print(f"{traco} Cálcular Sálario {traco}")

valor_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

total_salario = valor_por_hora*horas_trabalhadas

print(f"Total salário no referido mês e de R${total_salario:.2f}")
print(f"{traco} Fim do Programa {traco}")