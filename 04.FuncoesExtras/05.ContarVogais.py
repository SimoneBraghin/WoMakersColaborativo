"""INSTRUÇÕES: Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir umafrase e utilize a função para contar as vogais."""

# Criando a função que irá contar as vogais:
def contar_vogais (frase):
    cont = 0
    for letra in frase.lower():    # Percorre a frase em letras minúsculas verificando letra por letra
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':  # compara cada letra com as vogais
            cont += 1   # incrementa 1 para cada vogal localizada
    return cont

# Pedindo para que o usuário insira uma frase:
frase = input('Digite uma frase:\n')

# Chamando a função e imprimindo o resultado:
print(f'A frase digitada possui {contar_vogais(frase)} vogal(is).')   