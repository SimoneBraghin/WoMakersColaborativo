# Instruções 

'''
4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.

'''
pontuacao = float(input("Digite uma nota de 0 a 10: "))
situacao = ''

if pontuacao >= 7:
    situacao = 'aprovado'
else:
    situacao ='reprovado'
    
print(f'O aluno foi {situacao}')
    
