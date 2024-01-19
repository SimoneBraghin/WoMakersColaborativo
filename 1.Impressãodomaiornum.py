# Solicitamos o primeiro número ao usuário
numero1 = float(input("Por favor, insira o primeiro número: "))

# Solicitamos ao segundo número
numero2 = float(input("Por favor, insira o segundo número: "))

# Comparamos os números e exibimos o maior
if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os números são iguais.")