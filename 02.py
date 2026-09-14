def validar_nome(nome):
    return isinstance(nome, str) and nome.strip() != ""


def validar_idade(idade):
    try:
        idade = int(idade)
    except (ValueError, TypeError):
        return False
    return 14 <= idade <= 120


def validar_email(email):
    if not isinstance(email, str):
        return False

    email = email.strip()

    if "@" not in email:
        return False

    usuario, _, dominio = email.partition("@")

    if usuario == "" or dominio == "":
        return False

    if "." not in dominio:
        return False

    if dominio.startswith(".") or dominio.endswith("."):
        return False

    return True


def validar_senha(senha):
    return isinstance(senha, str) and len(senha) >= 8


def pedir_nome():
    while True:
        nome = input("Nome: ")
        if validar_nome(nome):
            return nome.strip()
        print("Nome não pode estar vazio.")


def pedir_idade():
    while True:
        idade = input("Idade: ")
        if validar_idade(idade):
            return int(idade)
        print("Idade deve estar entre 14 e 120.")


def pedir_email():
    while True:
        email = input("Email: ")
        if validar_email(email):
            return email.strip()
        print("Email inválido.")


def pedir_senha():
    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            return senha
        print("Senha deve ter pelo menos 8 caracteres.")


def cadastrar_usuario():
    print("Cadastro de Usuário")

    nome = pedir_nome()
    idade = pedir_idade()
    email = pedir_email()
    senha = pedir_senha()

    return {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha
    }


def main():
    usuario = cadastrar_usuario()

    print("\nCadastro concluído com sucesso")
    print(f"Nome:   {usuario['nome']}")
    print(f"Idade:  {usuario['idade']}")
    print(f"E-mail: {usuario['email']}")
    print(f"Senha:  {'*' * len(usuario['senha'])}")