'''
INSTRUÇÕES:
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''

# SOLICITA AO USÚARIO QUE DIGITE O TURNO DE ESTUDO

while True:
    turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

# CONDIÇÃO PARA IMPRIMIR A MENSAGEM APROPRIADA PRO TURNO DIGITADO COM BREAK 
    
    if turno.upper() == "M":
        print("Bom Dia!")
        break
    elif turno.upper() == "V":
        print("Boa Tarde!")
        break
    elif turno.upper() == "N":
        print("Boa Noite!")
        break
    else:
        print("Valor Inválido! Por favor, digite M, V ou N.")