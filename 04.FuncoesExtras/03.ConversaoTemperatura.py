"""INSTRUÇÕES: Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de 
conversão correta."""

# função que converte celsius para fahrenheit:
def celsiusFahrenheit(t):
    return t * 1.8 + 32

# função que converte fahrenheit para celsius:
def fahrenheitCelsius(t):
    return (t -32) / 1.8 

# Solicitando a escolha do tipo de conversão:
unidade = input('Com relação à temperatura informada você gostaria de: (inserir o número da opção desejada)\n1. Converter de grau Celsius para Fahrenheit\n2. Converter de Fahrenheit para grau Celsius\n')

# Laço para garantir que o usuário digite número válido:
while unidade != '1' and unidade != '2':  
    unidade = input('Valor inválido! Insira novamente o número da opção desejada:\n1. Converter de grau Celsius para Fahrenheit\n2. Converter de Fahrenheit para grau Celsius\n')

# Solicitando ao usuário que entre com o valor da temperatura:
temperatura = float(input('Digite a temperatura que você gostaria de converter: '))

# Chamando aas funções de acordo com o valor informado pelo usuário e imprimindo o resultado:
if unidade == '1':
    print(f'Resultado: {celsiusFahrenheit(temperatura):.1f}F')
else:
    print(f'Resultado: {fahrenheitCelsius(temperatura):.1f}ºC')
    