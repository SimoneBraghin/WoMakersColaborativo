'''
INSTRUÇÕES
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''
def DolarAmericano(carteira):
    calculo = carteira/4.91
    print(f'O usuário poderia comprar {calculo:.2f} dólares americanos.')

def PesoArgentino(carteira):
    calculo = carteira/0.02
    print(f'O usuário poderia comprar {calculo:.2f} pesos argentinos.')

def DolarAustraliano(carteira):
    calculo = carteira/3.18
    print(f'O usuário poderia comprar {calculo:.2f} dólares australianos.')

def DolarCanadense(carteira):
    calculo = carteira/3.64
    print(f'O usuário poderia comprar {calculo:.2f} dólares canadenses.')

def FrancoSuico(carteira):
    calculo = carteira/0.42
    print(f'O usuário poderia comprar {calculo:.2f} franco suiços.')

def Euro(carteira):
    calculo = carteira/5.36
    print(f'O usuário poderia comprar {calculo:.2f} euros.')

def LibraEsterlina(carteira):
    calculo = carteira/6.21
    print(f'O usuário poderia comprar {calculo:.2f} libras esterlinas.')

carteira = float(input("Por favor, digite quantos reais você possui em sua carteira: "))
DolarAmericano(carteira)
PesoArgentino(carteira)
DolarAustraliano(carteira)
DolarCanadense(carteira)
FrancoSuico(carteira)
Euro(carteira)
LibraEsterlina(carteira)
