"""INSTRUÇÕES: Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. 
Calcule o total do carrinho de compra."""


# Criando um dicionário:
listadecompras = {}

# Pedindo para o usuário adicionar um item a lista e informar o valor:
item = input('Adicione um item à lista: ')
valor = float(input('Informe o valor do item: R$'))  
listadecompras[item] = valor
fim = input('Gostaria de adicionar mais algum item (Sim-S e Não-N)? ')

# Loop para o usuário adicionar mais itens até digitar 'N':
while fim == 'S':    
    item = input('Adicione mais um item à lista: ')
    valor = float(input('Informe o valor do item: '))  
    listadecompras[item] = valor
    fim = input('Gostaria de adicionar mais algum item (Sim-S e Não-N)? ')

# Soma dos valores dos itens incluídos na lista de compras:
total = 0
for valor in listadecompras.values():
    total += valor

# Resultado formatado:
print(f'Valor total do carrinho: R$ {total:.2f}')