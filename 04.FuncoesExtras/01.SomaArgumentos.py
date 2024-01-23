"""INSTRUÇÕES:
Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos."""

def soma(arg1,arg2,arg3):
    resultado = arg1 + arg2 + arg3
    return print(f"O resultado é {resultado:.2f}")

input1 = float(input("informe primeiro valor para a soma: "))
input2 = float(input("informe segundo valor para a soma: "))
input3 = float(input("informe terceiro valor para a soma: "))

chamadaFuncao = soma(input1, input2, input3)