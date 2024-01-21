""" Instruções: Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""

idade = int(input('Digite sua idade: '))


if idade < 12 :
    print("Criança")
elif idade >= 12 and idade < 18:
    print("Adolescente")
elif idade >= 18 and idade < 65:
    print("Adulto")
elif idade >= 65:
    print("Idoso")

