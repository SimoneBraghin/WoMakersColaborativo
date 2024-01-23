'''
INSTRUÇÕES:
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

# PEDE AO USUÁRIO QUE DIGITE UMA NOTA ENTRE ZERO E DEZ

while True:
    try:
        nota = float(input("Digite uma nota entre zero e dez:"))
        
# VERIFICA SE A NOTA ESTÁ ENTRE ZERO E DEZ
        if 0 <= nota <= 10:
# SE A NOTA DIGITADA FOR ENTRE ZERO E DEZ EXIBE A NOTA E SAI DO LOOP
            print(f"Você digitou a nota {nota}")
            break  
# SE A NOTA NÃO FOR ENTRE ZERO E DEZ EXIBE MENSAGEM DE ERRO 
        else:   
            print(f"Nota inválida. Por favor, digite um valor entre zero e dez.")
# CASO O USUÁRIO DIGITAR UMA STRING SOLICITA UM VALOR NUMÉRICO NOVAMENTE
    except ValueError:
        print(f"Por favor, digite um valor numérico.")