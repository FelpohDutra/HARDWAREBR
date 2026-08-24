turma = {}

def adicionarAluno(classe):
    aluno = input("Digite a matricula do aluno: ")
    nomeAluno = input("Digite o nome do aluno: ")
    cidadeAluno = input("Digite a cidade do aluno: ")
    ingressoAluno = int(input("Digite o ano de ingresso que o aluno entrou: "))

    classe[aluno] = {
        "Nome": nomeAluno,
        "Cidade": cidadeAluno,
        "Ano de Ingresso": ingressoAluno
    }

    return classe

def lerTurma(classe):
    print(classe)

rep = 2

print("\n## Bem-vindo(a) ao sistema do IF ##\n- Para adicionar um aluno a turma, digite 1;")
while rep != 0:
    print("- Para ver as turmas digite 2;")
    print("- Para ver as o nome dos alunos digite 3;\n- Para ver alunos que ingressaram depois de 2023, digite 4.")
    print("- Para sair, digite 0.")

    rep = int(input())
    
    if rep == 1:
        turma = adicionarAluno(turma)
    elif rep == 2:
        lerTurma(f"\n{turma}")
    elif rep == 3:
        for informacoes in turma.values():
          print(informacoes["Nome"], )
    elif rep == 4:
        for informacoes in turma.values():
            if informacoes["Ano de Ingresso"]>=2023:
                print(f"{[informacoes["Nome"]]} : {informacoes["Ano de Ingresso"]}")
    else:
        print("Digite um numero valido")
        
print("\nAté mais.")
    
