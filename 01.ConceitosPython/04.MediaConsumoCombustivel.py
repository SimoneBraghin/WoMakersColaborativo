# Solicita a quantidade de litros de combustível e a distância percorrida ao usuário
litrosconsumidos = float(input("Por favor digite a quantidade de litros de combustível consumidos: "))
distanciapercorrida = float(input("Por favor, informe a distância percorrida em quilômetros: "))

# Calculo do consumo médio em km/l
consumomedio = distanciapercorrida / litrosconsumidos

# Exibe o resultado
print(f"O consumo médio é de {consumomedio:.2f} km/l")