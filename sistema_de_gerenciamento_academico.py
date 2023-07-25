import json
import random


def gerar_codigo() -> str:
    """
    Essa função gera um código aleatório de 9 dígitos.
    :return: Retorna um código de 9 dígitos.
    """
    return str(random.randint(100000000, 999999999))


def read_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_json(data: dict, file_path: str) -> None:
    """
    Essa função escreve em um arquivo json.
    :param data: Dados a serem escritos.
    :param file_path: Caminho do arquivo a ser escrito.
    :return: None
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
        f.close()


def cadastro_alunos() -> str:
    """
    Essa função estabelece o cadastro do aluno no sistema.
    É criada uma chave de acesso única ao aluno, com 9 dígitos.
    :return: Retorna que o aluno foi cadastrado com sucesso e seu número correspondente de matrícula.
    """
    matricula = gerar_codigo()
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    aluno = {"Matricula": matricula, "Nome": nome, "Curso": curso, "CPF": cpf}
    try:
        with open("alunos.json", "r") as f:
            alunos = json.load(f)
    except FileNotFoundError:
        alunos = {}
    alunos[matricula] = aluno
    write_json(alunos, "alunos.json")
    return f"Aluno cadastrado com sucesso! Matrícula: {matricula}"


def cadastro_professores() -> str:
    """
        Essa função estabelece o cadastro do professor no sistema.
        É criada uma chave de acesso única ao professor, com 9 dígitos.
        :return: Retorna que o professor foi cadastrado com sucesso e seu número correspondente de código.
    """
    codigo_prof = gerar_codigo()
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    professor = {"Codigo": codigo_prof, "Nome": nome, "CPF": cpf}
    try:
        with open("professores.json", "r") as f:
            professores = json.load(f)
    except FileNotFoundError:
        professores = {}
    professores[codigo_prof] = professor
    write_json(professores, "professores.json")
    return f"Professor cadastrado com sucesso! Código: {codigo_prof}"


def cadastro_disciplinas() -> str:
    """
        Essa função estabelece o cadastro da disciplina no sistema.
        É criada uma chave de acesso única à disciplina, com 9 dígitos.
        :return: Retorna que a disciplina foi cadastrada com sucesso e seu número correspondente de código.
    """
    codigo_disc = gerar_codigo()
    nome = input("Digite o nome do professor: ")
    disciplina = {"Codigo": codigo_disc, "Nome": nome}
    try:
        with open("disciplinas.json", "r") as f:
            disciplinas = json.load(f)
    except FileNotFoundError:
        disciplinas = {}
    disciplinas[codigo_disc] = disciplina
    write_json(disciplinas, "disciplinas.json")
    return f"Disciplina cadastrada com sucesso! Código: {codigo_disc}"


def cadastro_turmas() -> str:
    """
        Essa função estabelece o cadastro da disciplina no sistema.
        É criada uma chave de acesso única à disciplina, com 9 dígitos.
        :return: Retorna que a disciplina foi cadastrada com sucesso e seu número correspondente de código.
    """
    codigo_turma = gerar_codigo()
    codigo_prof = gerar_codigo()
    codigo_disc = gerar_codigo()
    turma = {"Codigo-turma": codigo_turma, "Codigo-prof": codigo_prof, "Codigo-disc": codigo_disc}
    try:
        with open("turmas.json", "r") as f:
            turmas = json.load(f)
    except FileNotFoundError:
        turmas = {}
    turmas[codigo_turma] = turma
    write_json(turmas, "turmas.json")
    return f"Turma cadastrada com sucesso! Código: {codigo_turma}"


def cadastro_matriculas():
    """
        Essa função estabelece o cadastro da matricula no sistema.
        É criada uma chave de acesso única à matricula, com 9 dígitos.
        :return: Retorna que a matricula foi cadastrada com sucesso e seu número correspondente de código.
    """
    codigo_turma = gerar_codigo()
    codigo_aluno = gerar_codigo()
    matricula = {"Matricula": codigo_aluno, "Codigo": codigo_turma}
    try:
        with open("matriculas.json", "r") as f:
            matriculas = json.load(f)
    except FileNotFoundError:
        matriculas = {}
    matriculas[codigo_turma] = matricula
    write_json(matriculas, "matriculas.json")


def listar_alunos(path='alunos.json'):
    alunos = read_json(path)
    if not alunos:
        print("Não existem alunos cadastrados!")
    else:
        for matricula, dados in alunos.items():
            print(f"Nome: {dados['Nome']}, Matrícula: {matricula}, Curso: {dados['Curso']}, CPF: {dados['CPF']}")


def listar_professores(path='professores.json'):
    professores = read_json(path)
    if not professores:
        print("Não existem professores cadastrados!")
    else:
        for codigo_prof, dados in professores.items():
            print(f"Nome: {dados['Nome']}, Matrícula: {codigo_prof}, CPF: {dados['CPF']}")


def listar_disciplinas(path='disciplinas.json'):
    disciplinas = read_json(path)
    if not disciplinas:
        print("Não existem professores cadastrados!")
    else:
        for codigo_disc, dados in disciplinas.items():
            print(f"Código: {codigo_disc}, Nome: {dados['Nome']}")


def listar_turmas(path='turmas.json'):
    turmas = read_json(path)
    if not turmas:
        print("Não existem professores cadastrados!")
    else:
        for codigo_turma, dados in turmas.items():
            print(
                f"Código da turma: {codigo_turma}, Código do professor: {dados['codigo_prof']}, Código da disciplina: {dados['codigo_disc']}")


def listar_matriculas(path='matriculas.json'):
    matriculas = read_json(path)
    if not matriculas:
        print("Não existem professores cadastrados!")
    else:
        for codigo_turma, dados in matriculas.items():
            print(f"Código da turma: {codigo_turma}, Matrícula do aluno: {dados['matricula']}")


def alterar_dados_aluno(path='alunos.json'):
    matricula = input("Digite a matrícula do aluno que deseja alterar os dados: ")
    alunos = read_json(path)
    if matricula in alunos:
        nome = input(f"Digite o nome do aluno ({alunos[matricula]['Nome']}): ")
        curso = input(f"Digite o novo curso do aluno ({alunos[matricula]['Curso']}): ")
        cpf = input(f"Digite o CPF do aluno ({alunos[matricula]['CPF']}): ")
        alunos[matricula]["Nome"] = nome
        alunos[matricula]["Curso"] = curso
        alunos[matricula]["CPF"] = cpf
        write_json(alunos, path)
        print("Dados do aluno alterados com sucesso!")
    else:
        print("Matrícula não encontrada.")


def alterar_dados_professor(path='professores.json'):
    codigo_prof = input("Digite o código do professor que deseja alterar os dados: ")
    professores = read_json(path)
    if codigo_prof in professores:
        nome = input(f"Digite o nome do professor ({professores[codigo_prof]['Nome']}): ")
        cpf = input(f"Digite o CPF do professor ({professores[codigo_prof]['CPF']}): ")
        professores[codigo_prof]["Nome"] = nome
        professores[codigo_prof]["CPF"] = cpf
        write_json(professores, path)
        print("Dados do professor alterados com sucesso!")
    else:
        print("Código do professor não encontrado.")


def alterar_dados_disciplina(path='disciplinas.json'):
    codigo_disc = input("Digite o código da disciplina deseja alterar o nome: ")
    disciplinas = read_json(path)
    if codigo_disc in disciplinas:
        nome = input(f"Digite o nome da disciplina ({disciplinas[codigo_disc]['Nome']}): ")
        disciplinas[codigo_disc]["Nome"] = nome
        write_json(disciplinas, path)
        print("Dados da disciplina alterados com sucesso!")
    else:
        print("Código da disciplina não encontrado.")


def alterar_dados_turma(path='turmas.json'):
    codigo_turma = input("Digite o código da turma deseja alterar as informações: ")
    turmas = read_json(path)
    if codigo_turma in turmas:
        codigo_turma_novo = input(f"Digite o código da turma ({turmas[codigo_turma]}): ")
        codigo_prof_novo = input(f"Digite o código do professor ({turmas[codigo_turma]['Codigo-prof']}): ")
        codigo_disc_novo = input(f"Digite o código da disciplina ({turmas[codigo_turma]['Codigo-disc']}): ")
        turmas[codigo_turma]["Codigo-turma"] = codigo_turma_novo
        turmas[codigo_turma]["Codigo-prof"] = codigo_prof_novo
        turmas[codigo_turma]["Codigo-disc"] = codigo_disc_novo
        write_json(turmas, path)
        print("Dados da disciplina alterados com sucesso!")
    else:
        print("Código da disciplina não encontrado.")


def alterar_dados_matricula(path='matriculas.json'):
    codigo_aluno = input("Digite a matrícula deseja alterar: ")
    matriculas = read_json(path)
    if codigo_aluno in matriculas:
        codigo_turma_novo = input(f"Digite o código da turma ({matriculas[codigo_aluno]['Codigo']}): ")
        codigo_aluno_novo = input(f"Digite o código da disciplina ({matriculas[codigo_aluno]['Matricula']}): ")
        matriculas[codigo_aluno]["Matricula"] = codigo_turma_novo
        matriculas[codigo_aluno]["Codigo"] = codigo_aluno_novo
        write_json(matriculas, path)
        print("Dados da matrícula alterados com sucesso!")
    else:
        print("Matrícula não encontrada.")


def excluir_aluno(path='alunos.json'):
    matricula = input("Qual a matrícula do aluno a ser excluído?")
    alunos = read_json(path)
    if matricula in alunos:
        del alunos[matricula]['Nome']
        del alunos[matricula]['Curso']
        del alunos[matricula]['CPF']
        del alunos[matricula]
        write_json(alunos, path)
        print("Aluno excluído com sucesso")
    else:
        print("Não existe aluno cadastrado com essa matrícula")


def excluir_professor(path='professores.json'):
    codigo_prof = input("Qual o código do professor a ser excluído?")
    professores = read_json(path)
    if codigo_prof in professores:
        del professores[codigo_prof]['Nome']
        del professores[codigo_prof]['CPF']
        del professores[codigo_prof]
        write_json(professores, path)
        print("Professor excluído com sucesso")
    else:
        print("Não existe professor cadastrado com esse código")


def excluir_disciplina(path='disciplinas.json'):
    codigo_disc = input("Qual o código da disciplina a ser excluída?")
    disciplinas = read_json(path)
    if codigo_disc in disciplinas:
        del disciplinas[codigo_disc]['Nome']
        del disciplinas[codigo_disc]
        write_json(disciplinas, path)
        print("Disciplina excluída com sucesso")
    else:
        print("Não existe disciplina cadastrada com esse código")


def excluir_turma(path='turmas.json'):
    codigo_turma = input("Qual o código da turma a ser excluída?")
    turmas = read_json(path)
    if codigo_turma in turmas:
        del turmas[codigo_turma]['Codigo-prof']
        del turmas[codigo_turma]['Codigo-disc']
        del turmas[codigo_turma]
        write_json(turmas, path)
        print("Turma excluída com sucesso")
    else:
        print("Não existe turma cadastrada com esse código")


def excluir_matricula(path='matriculas.json'):
    matricula = input("Qual a matricula a ser excluída?")
    matriculas = read_json(path)
    if matricula in matriculas:
        del matriculas[matricula]['codigo_turma']
        del matriculas[matricula]['codigo_aluno']
        del matriculas[matricula]
        write_json(matriculas, path)
        print("Matrícula excluída com sucesso")
    else:
        print("Não existe Matrícula cadastrada com esse código")


def menu_estudantes():
    print("** (ESTUDANTES) MENU DE OPERAÇÕES **\n")
    print("(1) Incluir estudante")
    print("(2) Listas estudantes")
    print("(3) Atualizar um estudante")
    print("(4) Excluir um estudante")
    print("(0) Sair\n")
    opcao_estud = int(input("Informe a ação desejada: \n"))

    if opcao_estud == 1:
        cadastro_alunos()
        print()
    elif opcao_estud == 2:
        listar_alunos(path='alunos.json')
        print()
    elif opcao_estud == 3:
        alterar_dados_aluno(path='alunos.json')
        print()
    elif opcao_estud == 4:
        excluir_aluno(path='alunos.json')
        print()
    else:
        print("Encerrando o seu atendimento!\n")
        exit()


def menu_professores():
    print("** (PROFESSORES) MENU DE OPERAÇÕES **\n")
    print("(1) Incluir professor\n"
          "(2) Listar professores\n"
          "(3) Atualizar um professor\n"
          "(4) Excluir um professor\n"
          "(0) Sair\n")
    opcao_prof = int(input("Informe a ação desejada: \n"))

    if opcao_prof == 1:
        cadastro_professores()
        print()
    elif opcao_prof == 2:
        listar_professores(path='professores.json')
        print()
    elif opcao_prof == 3:
        alterar_dados_professor(path='professores.json')
        print()
    elif opcao_prof == 4:
        excluir_professor(path='professores.json')
        print()
    else:
        print("Encerrando o seu atendimento!\n")
        exit()


def menu_disciplinas():
    print("** (DISCIPLINAS) MENU DE OPERAÇÕES **\n")
    print("(1) Incluir disciplinas\n"
          "(2) Listar disciplinas\n"
          "(3) Atualizar uma disciplina\n"
          "(4) Excluir uma disciplina\n"
          "(0) Sair\n")
    opcao_disc = int(input("Informe a ação desejada: \n"))

    if opcao_disc == 1:
        cadastro_disciplinas()
        print()
    elif opcao_disc == 2:
        listar_disciplinas(path="disciplinas.json")
        print()
    elif opcao_disc == 3:
        alterar_dados_disciplina(path="disciplinas.json")
        print()
    elif opcao_disc == 4:
        excluir_disciplina(path="disciplinas.json")
        print()
    else:
        print("Encerrando o seu atendimento!\n")
        exit()


def menu_turmas():
    print("** (TURMAS) MENU DE OPERAÇÕES **\n")
    print("(1) Incluir turmas\n"
          "(2) Listar turmas\n"
          "(3) Atualizar uma turma\n"
          "(4) Excluir uma turma\n"
          "(0) Sair\n")
    opcao_turmas = int(input("Informe a ação desejada: \n"))

    if opcao_turmas == 1:
        cadastro_turmas()
        print()
    elif opcao_turmas == 2:
        listar_turmas(path="turmas.json")
        print()
    elif opcao_turmas == 3:
        alterar_dados_disciplina(path="turmas.json")
        print()
    elif opcao_turmas == 4:
        excluir_disciplina(path="turmas.json")
        print()
    else:
        print("Encerrando o seu atendimento!\n")
        exit()


def menu_matriculas():
    print("** (MATRÍCULAS) MENU DE OPERAÇÕES **\n")
    print("(1) Incluir matrícula\n"
          "(2) Listar matrículas\n"
          "(3) Atualizar uma matrícula\n"
          "(4) Excluir uma matrícula\n"
          "(0) Sair\n")
    opcao_matric = int(input("Informe a ação desejada: \n"))

    if opcao_matric == 1:
        cadastro_matriculas()
        print()
    elif opcao_matric == 2:
        listar_matriculas(path="matriculas.json")
        print()
    elif opcao_matric == 3:
        alterar_dados_matricula(path="matriculas.json")
        print()
    elif opcao_matric == 4:
        excluir_matricula(path="matriculas.json")
        print()
    else:
        print("Encerrando o seu atendimento!\n")
        exit()


while True:
    print("** MENU DE OPERAÇÕES **\n")
    print("(1) Gerenciar estudantes")
    print("(2) Gerenciar professores")
    print("(3) Gerenciar disciplinas")
    print("(4) Gerenciar turmas")
    print("(5) Gerenciar matrículas")
    print("(0) Sair\n")
    opcao = int(input("Qual das opções acima você deseja acessar?\n"))

    if opcao == 1:
        menu_estudantes()
    elif opcao == 2:
        menu_professores()
    elif opcao == 3:
        menu_disciplinas()
    elif opcao == 4:
        menu_turmas()
    elif opcao == 5:
        menu_matriculas()
    elif opcao == 6:
        print("Em desenvolvimento.\n")
    elif opcao == 0:
        print("Encerrando o seu atendimento.\n")
        break