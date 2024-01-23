"""INSTRUÇÕES:
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721."""

numeroInteiro = "Incorreto"

try:
    numeroInteiro = int(input("Informe um número inteiro: "))
except:
    print("Valor incorreto: reinicie o programa e informe um número inteiro")

def reverse(numeroInteiro):
    numeroString = str(numeroInteiro)
    reverterNum = numeroString[::-1]
    return print(f"O Resultado da reversão de {numeroInteiro} é {reverterNum}")

if numeroInteiro == "Incorreto":
    print("--- Finalizado ---")
else:
    resultado = reverse(numeroInteiro)