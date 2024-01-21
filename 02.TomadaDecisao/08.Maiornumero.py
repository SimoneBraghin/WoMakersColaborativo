""" Instruções: Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
"""

valor1 = str(input('Digite o primeiro número: '))
valor2 = str(input('Digite o segundo número: '))
valor3 = str(input('Digite o terceiro número: '))

numeros = [valor1.replace(".", "").replace(",", "."), valor2.replace(".", "").replace(",", "."), valor3.replace(".", "").replace(",", ".")]

print(f"O maior numero é: ",max(float(number) for number in numeros))