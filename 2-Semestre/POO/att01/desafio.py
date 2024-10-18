turma=list()
while True:
    nome=input("Digite o nome do aluno: ")
    notas=list()
    media=0.0
    for i in range(0,3):
        notas.append(int(input(f"Digite a {i+1}° nota: ")))
        media+=notas[i]
    aluno={'nome':nome,'notas':notas,'Média':media/3}
    turma.append(aluno)
    r=input("Quer adicionar mais alunos? [S/N] ")
    if r in 'Nn':
        break
print(turma)