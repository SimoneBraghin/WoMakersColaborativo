'''
INSTRUÇÕES:
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade.

'''

# DEFININDO AS VARIAVEIS

nome = input(f'Digite seu nome:')
cidade = input(f'Digite a cidade que você mora:')
musica = input(f'Digite seu gênero musical favorito:')
banda = input(f'Agora coloque sua banda predileta:')

# CRIANDO A MENSAGEM AMIGÁVEL

mensagem = f"Oi {nome}, que bom te ver aqui. Que legal que você mora em {cidade}, gostaria de conhecer. Seu gosto musical em {musica} não se discute, mas o meu é melhor. E com um gosto musical desses sabia que sua banda predileta {banda} não iria desapontar."

# PRINT DA MENSAGEM

print(mensagem)