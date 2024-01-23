""" INSTRUÇÕES:
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
    As perguntas são:
        ""Telefonou para a vítima?""
        ""Esteve no local do crime?""
        ""Mora perto da vítima?""
        ""Devia para a vítima?""
        ""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente:
2 questões ela deve ser classificada como ""Suspeita"", 
entre 3 e 4 como ""Cúmplice"", e 
5 como ""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
"""

print("\n==========JOGO DETETIVE==========\n")
print("""Em um cenário sombrio, onde a intriga e o mistério permeiam os corredores de um local misterioso, um assassinato chocante deixou todos atônitos. 
Você, caro jogador, emerge como o principal suspeito nesse macabro quebra-cabeça. 
O lendário detetive Sherlock Holmes, da Scotland Yard, assume as rédeas da investigação e convoca, um a um, todos os envolvidos para um interrogatório crucial...
O momento chegou! 
Sob uma atmosfera tensa e suspeitas que pairam no ar, você se encontra diante de Holmes, pronto para responder às suas perguntas.
A sinceridade será sua maior aliada, pois qualquer deslize pode resultar em graves acusações de obstrução da justiça e cumplicidade no horrendo crime. 
Desvende a verdade, prove sua inocência e descubra se, no final das contas, você é o herói da história ou o culpado astuto que todos buscam. 
O destino aguarda suas respostas neste intrigante jogo de investigação.""")
print("\n-----VAMOS COMEÇAR O SEU INTERROGATÓRIO!!!-----\n")

def classificador(telefonouVitima, esteveLocalCrime, morarProximoVitima, dividaAtiva, trabalhouComVitima):
    classificacaoSuspeito = ["Inocente",'Inocente','Suspeito', "Cúmplice", "Cúmplice", "o Assassino"]
    resultado = telefonouVitima + esteveLocalCrime + morarProximoVitima + dividaAtiva + trabalhouComVitima
    
    return print(f"Sherlock Holmes deduziu que você é {classificacaoSuspeito[resultado]}")

print("Este é uma interrogatório investigativo com base na parapsicologia de Jung! \nVocê tem que responder as perguntas com [1] para Sim ou [0] para Não. \nVamos começar!!!\n")

interrogatorio = True

while interrogatorio == True:
    try:    
        telefonouVitima = int(input("Você telefonou para a vítima no dia do crime? [1] Sim ou [0] Não? \nResposta >>> "))
        if telefonouVitima not in [1,0]:
            print("Essa opção não existe.\nFavor responder 1 para Sim e 0 para Não")
            continue
        esteveLocalCrime = int(input("Você esteve no local do crime no dia do crime? [1] Sim ou [0] Não? \nResposta >>> "))
        if esteveLocalCrime not in [1,0]:
            print("Essa opção não existe.\nFavor responder 1 para Sim e 0 para Não")
            continue
        morarProximoVitima = int(input("Você mora perto da vítima? [1] Sim ou [0] Não? \nResposta >>> "))
        if morarProximoVitima not in [1,0]:
            print("Essa opção não existe.\nFavor responder 1 para Sim e 0 para Não")
            continue
        dividaAtiva = int(input("Você devia dinheiro ou algo além para a vítima? [1] Sim ou [0] Não? \nResposta >>> "))
        if dividaAtiva not in [1,0]:
            print("Essa opção não existe.\nFavor responder 1 para Sim e 0 para Não")
            continue
        trabalhouComVitima= int(input("Você já trabalhou com a vítima? [1] Sim ou [0] Não? \nResposta >>> "))
        if trabalhouComVitima not in [1,0]:
            print("Essa opção não existe.\nFavor responder 1 para Sim e 0 para Não")
            continue
        interrogatorio = False
    except ValueError:
        print("Você não está levando este interrogatório a sério! Se não responder corretamente iremos considerá-lo Cúmplice do crime!\n")


perguntas = [telefonouVitima, esteveLocalCrime, morarProximoVitima, dividaAtiva, trabalhouComVitima]
conclusaoSherlockHomes = classificador(telefonouVitima, esteveLocalCrime, morarProximoVitima, dividaAtiva, trabalhouComVitima)