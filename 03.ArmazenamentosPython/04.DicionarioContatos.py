"""INSTRUÇÕES: Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome."""

# Criando o dicionário:
contatos = {}
contatos ['Ana'] = '11 91234 5678'
contatos ['Bruno'] = '12 92345 6789'
contatos ['Camila'] = '13 93456 7890'
contatos ['Danilo'] = '14 99876 5432'
contatos ['Eduardo'] = '15 98765 4321'
contatos ['Flávia'] = '16 97654 3210'

# Pedindo para o usuário entrar com o nome do contato:
busca = input('Digite o nome do contato: ')

# Realizando a busca pelos itens do dicionário:
encontrado = False   # Criei uma variável em boolean para verificar se o contato está ou não no dicionáro e atribui o valor false
for nome, numero in contatos.items():
    if nome == busca:
        print(f'Segue o contato solicitado: {nome} - {numero}')
        encontrado = True
        break # Caso for encontrado, será atribuído o valor true à variável 'encontrado' e a repetição irá ser interrompida

# Uma mensagem para caso o contato não for encontrado    
if not encontrado:
    print(f'O contato com o nome {busca} não foi encontrado!')