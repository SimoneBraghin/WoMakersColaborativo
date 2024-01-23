'''
INSTRUÇÕES:
Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

'''

# PEDE AO USUÁRIO QUE DIGITE LOGIN E SENHA 
login = input("Digite seu login:")
senha = input("Digite sua senha:")

# VERIFICA SE A INFORMAÇÃO ESTÁ CORRETA
if login == "admin" and senha == "admin123":
    print(f"Acesso permitido. Bem-vindo, admin!")
# CASO NÃO SEJA O LOGIN E SENHA CORRETOS EXIBE MENSAGEM DE ERRO E ENCERRA O PROGRAMA
else:
    print(f"Erro: Login ou senha incorretos. Acesso negado.")
