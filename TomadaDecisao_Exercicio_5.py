'''
5 - Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e 
classifique-o com o equilátero, isósceles ou escaleno. 
	equilátero: todos os lados com o mesmo valor 
	isósceles: dois lados com o mesmo valor 
	escaleno: todos os lados com medidas distintas.
'''
lado1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
lado2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
lado3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))

if lado1 == lado2 == lado3:
    print('Triângulo de todos lados de mesmo valor é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo que possui dois lados de mesmo valor é isósceles.')  
else:
    print('Triângulo que possui lados distintos é escaleno.')