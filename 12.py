class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def apresentar_dados(self):
        print("Nome:", self.nome)
        print("Data de nascimento:", self.data_nascimento)


class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, curso):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            print("A nota deve estar entre 0 e 10.")
            return

        self.notas.append(nota)
        print("Nota adicionada com sucesso!")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)

    def apresentar_dados(self):
        print("\n===== DADOS DO ALUNO =====")
        super().apresentar_dados()
        print("Matrícula:", self.matricula)
        print("Curso:", self.curso)
        print("Notas:", self.notas)
        print(f"Média: {self.calcular_media():.2f}")


class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, disciplina):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.disciplina = disciplina

    def apresentar_dados(self):
        print("\n===== DADOS DO PROFESSOR =====")
        super().apresentar_dados()
        print("Matrícula:", self.matricula)
        print("Disciplina:", self.disciplina)


def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ")
    data_nascimento = input("Data de nascimento: ")
    matricula = input("Matrícula: ")

    for aluno in alunos:
        if aluno.matricula == matricula:
            print("Essa matrícula já está cadastrada!")
            return

    curso = input("Curso: ")

    aluno = Aluno(nome, data_nascimento, matricula, curso)
    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def cadastrar_professor(professores):
    nome = input("Nome do professor: ")
    data_nascimento = input("Data de nascimento: ")
    matricula = input("Matrícula: ")

    for professor in professores:
        if professor.matricula == matricula:
            print("Essa matrícula já está cadastrada!")
            return

    disciplina = input("Disciplina: ")

    professor = Professor(
        nome, data_nascimento, matricula, disciplina
    )

    professores.append(professor)
    print("Professor cadastrado com sucesso!")


def buscar_aluno(alunos):
    matricula = input("Digite a matrícula do aluno: ")

    for aluno in alunos:
        if aluno.matricula == matricula:
            return aluno

    print("Aluno não encontrado.")
    return None


def buscar_professor(professores):
    matricula = input("Digite a matrícula do professor: ")

    for professor in professores:
        if professor.matricula == matricula:
            return professor

    print("Professor não encontrado.")
    return None


def adicionar_nota_aluno(alunos):
    aluno = buscar_aluno(alunos)

    if aluno is None:
        return

    try:
        nota = float(input("Digite a nota (0 a 10): "))
        aluno.adicionar_nota(nota)
    except ValueError:
        print("Digite uma nota numérica válida.")


def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        aluno.apresentar_dados()


def listar_professores(professores):
    if len(professores) == 0:
        print("Nenhum professor cadastrado.")
        return

    for professor in professores:
        professor.apresentar_dados()


def main():
    alunos = []
    professores = []

    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar professor")
        print("3 - Listar alunos")
        print("4 - Listar professores")
        print("5 - Adicionar nota a aluno")
        print("6 - Consultar aluno e média")
        print("7 - Consultar professor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno(alunos)

        elif opcao == "2":
            cadastrar_professor(professores)

        elif opcao == "3":
            listar_alunos(alunos)

        elif opcao == "4":
            listar_professores(professores)

        elif opcao == "5":
            adicionar_nota_aluno(alunos)

        elif opcao == "6":
            aluno = buscar_aluno(alunos)

            if aluno is not None:
                aluno.apresentar_dados()

        elif opcao == "7":
            professor = buscar_professor(professores)

            if professor is not None:
                professor.apresentar_dados()

        elif opcao == "0":
            print("Encerrando o sistema escolar...")
            break

        else:
            print("Opção inválida!")

main()