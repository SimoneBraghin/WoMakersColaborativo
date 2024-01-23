""" Instruções: Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
"""

valor1 = int(input('Digite um número ')) 
valor2 = int(input('Digite outro número ')) 
valor3 = int(input('Digite o ultimo número ')) 

numeros =[valor1, valor2, valor3]
print(f"A ordem crescente é: ", sorted(numeros))