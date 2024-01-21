"""INSTRUÇÕES:
Vamos construir um jogo de forca.

O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida.

A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas.

Em cada tentativa, o jogador pode fornecer uma letra.
Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes.
Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada.
Após um número máximo de erros, o jogador perde.
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas."""

import random

def jogo_forca():
    lista_palavras = ['carrinho', 'bola', 'boneca', 'biclicleta', 'patinete']
    palavra_secreta = random.choice(lista_palavras)
    palavra_exibida = ['_' for _ in palavra_secreta]
    tentativas = 6

    print('Bem-vindo ao jogo da forca!')
    print('A palavra secreta é: ', ' '.join(palavra_exibida))
    print('Você tem ', tentativas, ' tentativas restantes.')

    while tentativas > 0 and '_' in palavra_exibida:
        letra = input('Por favor, digite uma letra: ')

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_exibida[i] = letra
            print('A palavra secreta é: ', ' '.join(palavra_exibida))
        else:
            tentativas -= 1
            print('Letra errada. Você agora tem ', tentativas, ' tentativas restantes.')

    if '_' not in palavra_exibida:
        print('Muito bem!!!!, você venceu!!!!')
    else:
        print('Que pena, você perdeu. A palavra secreta era ', palavra_secreta)

jogo_forca()