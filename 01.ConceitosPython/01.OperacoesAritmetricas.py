"""INSTRUÇÕES:
1. Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
"""


print("=========Calculadora iniciada!=========")

while True:
    print("Selecione os números que deseja calcular:")
    num1 = float(input("Informe o primeiro número: >>>"))
    num2 = float(input("Informe o segundo número: >>>"))

    try:
        operacao = int(input("Selecione o tipo de operação que deseja realizar:\n [1] Soma \n [2] Subtração \n [3] Multiplicação \n [4] Divisão \n [0] Encerrar Calculadora \n>>>"))
        match operacao:
            case 1:
                resultado = num1 + num2
                print(f"O resultado da operação é {resultado}")
                novaOperacao = int(input("\nDeseja fazer nova operação?\n[1] Sim \n[0] Não\n>>>"))
                if novaOperacao == 1:
                        print("Reiniciando a calculadora...")
                elif novaOperacao == 0:
                        print("Programa encerrado!")
                        break
                else:
                    print("Valor inválido. \nEncerrando")
                    break                
            case 2:
                resultado = num1 - num2
                print(f"O resultado da operação é {resultado}")
                novaOperacao = int(input("\nDeseja fazer nova operação?\n[1] Sim \n[0] Não\n>>>"))
                if novaOperacao == 1:
                        print("Reiniciando a calculadora...")
                elif novaOperacao == 0:
                        print("Programa encerrado!")
                        break
                else:
                    print("Valor inválido. \nEncerrando")
                    break
            case 3:
                resultado = num1 * num2
                print(f"O resultado da operação é {resultado}")
                novaOperacao = int(input("\nDeseja fazer nova operação?\n[1] Sim \n[0] Não\n>>>"))
                if novaOperacao == 1:
                        print("Reiniciando a calculadora...")
                elif novaOperacao == 0:
                        print("Programa encerrado!")
                        break
                else:
                    print("Valor inválido. \nEncerrando")
                    break
            case 4:
                resultado = num1 // num2
                print(f"O resultado da operação é {resultado}")
                novaOperacao = int(input("\nDeseja fazer nova operação?\n[1] Sim \n[0] Não\n>>>"))
                if novaOperacao == 1:
                        print("Reiniciando a calculadora...")
                elif novaOperacao == 0:
                        print("Programa encerrado!")
                        break
                else:
                    print("Valor inválido. \nEncerrando")
                    break
            case 0:
                print("Programa encerrado!")
                break
    except:
        print("Valor informado não é válido. \nReiniciando a calculadora...\n")

