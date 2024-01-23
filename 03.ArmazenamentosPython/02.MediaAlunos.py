'''
INSTRUÇÕES:
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
'''
media_todos = []

for counter in range(5):
    notas_alunos = []
    
    for aux in range(4):
                nota = float(input(f'Digite a {aux+1}ª nota do {counter+1}º aluno: '))
                notas_alunos.append(nota)
    
    media = float(sum(notas_alunos)/len(notas_alunos))
    media_todos.append(media)
    print("---------------------------------------------------")

aprovacoes = 0
for medias in media_todos:
    if medias >= 7.0:
        aprovacoes+=1

print(f'A quantidade de alunos com media maior ou igual a 7 foi: {aprovacoes} alunos.')