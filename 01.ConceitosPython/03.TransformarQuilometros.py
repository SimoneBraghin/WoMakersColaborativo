# Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
# Para iniciar informe os quilometros
quilometros = float(input("Informe por favor a quantidade de quilômetros: "))

# Esse calculo transforma quilômetros em metros
metros = quilometros * 1000

# Quilômetros em centímetros
centimetros = quilometros * 1000000

# Quilômetros em milímetros
milimetros = quilometros * 1000000

# Exibirá os resultados da seguinte forma
print(f"{quilometros} quilômetros corresponde a {metros} metros.")
print(f"{quilometros} quilômetros correspode a {centimetros} centímetros.")
print(f"{quilometros} quilômetros corresponde a {milimetros} milímetros.")