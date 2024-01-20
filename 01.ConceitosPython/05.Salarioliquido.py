""" Instruções: Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda. """


from unittest import case


print("----- Calcule seu salario liquido -----")

while True:
        valor = str(input("Informe seu salario bruto: "))
        salario = float(valor.replace(".", "").replace(",", "."))
        alq = 0
        
        case
        if salario <= 1903.98 :
                print(f"O seu salario é isento de imposto de renda! \n O valor a receber é: {salario} reais")
                novocalculo = int(input("\nDeseja realizar um novo calculo?\n 1 Sim \n 0 Não\n>>>"))
                if novocalculo == 1:
                        print("Reiniciando")
                elif novocalculo == 0:
                        print("Obrigado!")
                        break
                else:
                    print("Valor inválido. \n Obrigada!")
                    break                
        case
        if salario >= 1903.99 and salario <= 2826.65 :
                alq = 7.5
                calculo = (salario*alq)/100
                saliq = salario - calculo
                print(f"Sua aliquota de imposto de renda é: {alq}%! \n O valor a receber é: {saliq:.2f} reais")
                novocalculo = int(input("\nDeseja realizar um novo calculo?\n 1 Sim \n 0 Não\n>>>"))
                if novocalculo == 1:
                        print("Reiniciando")
                elif novocalculo == 0:
                        print("Obrigado!")
                        break
                else:
                    print("Valor inválido. \n Obrigada!")
                    break            
        case
        if salario >= 2826.66 and salario <= 3751.05 :
                alq = 15
                calculo = (salario*alq)/100
                saliq = salario - calculo
                print(f"Sua aliquota de imposto de renda é: {alq}%! \n O valor a receber é: {saliq:.2f} reais")
                novocalculo = int(input("\nDeseja realizar um novo calculo?\n 1 Sim \n 0 Não\n>>>"))
                if novocalculo == 1:
                        print("Reiniciando")
                elif novocalculo == 0:
                        print("Obrigado!")
                        break
                else:
                    print("Valor inválido. \n Obrigada!")
                    break    
        case
        if salario >= 3751.06 and salario <= 4664.68 :
                alq = 22.5
                calculo = (salario*alq)/100
                saliq = salario - calculo
                print(f"Sua aliquota de imposto de renda é: {alq}%! \n O valor a receber é: {saliq:.2f} reais")
                novocalculo = int(input("\nDeseja realizar um novo calculo?\n 1 Sim \n 0 Não\n>>>"))
                if novocalculo == 1:
                        print("Reiniciando")
                elif novocalculo == 0:
                        print("Obrigado!")
                        break
                else:
                    print("Valor inválido. \n Obrigada!")
                    break      
        case
        if salario > 4664.68 :
                alq = 27.5
                calculo = (salario*alq)/100
                saliq = salario - calculo
                print(f"Sua aliquota de imposto de renda é: {alq}%! \n O valor a receber é: {saliq:.2f} reais")
                novocalculo = int(input("\nDeseja realizar um novo calculo?\n 1 Sim \n 0 Não\n>>>"))
                if novocalculo == 1:
                        print("Reiniciando")
                elif novocalculo == 0:
                        print("Obrigado!")
                        break
                else:
                    print("Valor inválido. \n Obrigada!")
                    break               
                



"""
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
"""