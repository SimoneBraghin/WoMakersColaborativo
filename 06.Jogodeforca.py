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