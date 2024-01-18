aux = 1
par = []
impar = []

while aux != 0:
    num = float(input("Digite um número: "))
    
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    aux = int(input("Deseja continuar? Tecle 0 para Encerrar ou 1 para continuar: "))

qnt_par = len(par)
qnt_impar = len(impar)

print(f'A quantidade números pares é {qnt_par} e quantidade de números ímpares é {qnt_impar}.')
    

