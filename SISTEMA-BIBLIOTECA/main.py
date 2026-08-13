# Sistema de Gerenciamento de Biblioteca
livros = []

def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("\nCadastro de livro")
    elif opcao == "2":
        print("\nEmpréstimo de livro")
    elif opcao == "3":
        print("\nDevolução de livro")
    elif opcao == "4":
        print("\nLista de livros")
    elif opcao == "5":
        print("\nBusca de livro")
    elif opcao == "6":
        print("\nOrdenação de livros")
    elif opcao == "7":
        print("\nPrograma encerrado.")
        break
    else:
        print("\nOpção inválida!")
        import csv
ARQUIVO = "livros.csv"

def carregar_livros():
    """Carrega os livros salvos no arquivo CSV."""
    livros = []
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)
    except FileNotFoundError:
    # Se o arquivo ainda não existir, começa com uma lista vazia.
        livros = []
    return livros

def salvar_livros(livros):
    """Salva todos os livros no arquivo CSV."""
    campos = ["titulo", "autor", "ano", "isbn", "status"]
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)

def cadastrar_livro(livros):
    """Cadastra um novo livro."""
    print("\n===== CADASTRO DE LIVRO =====")
    titulo = input("Título: ")
    autor = input("Autor: ")
    try:
        ano = int(input("Ano de publicação: "))
    except ValueError:
        print("Ano inválido.")
        return livros
    isbn = input("Código/ISBN: ")
    # Verifica se já existe um livro com o mesmo ISBN.
    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro cadastrado com esse ISBN.")
            return livros
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }
    livros.append(novo_livro)
    salvar_livros(livros)
    print("Livro cadastrado com sucesso!")
    return livros

def encontrar_livro(livros, isbn):
    """Procura um livro pelo ISBN."""
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
    return None

def emprestar_livro(livros):
    """Registra o empréstimo de um livro."""
    print("\n===== EMPRÉSTIMO =====")
    isbn = input("Digite o ISBN do livro: ")
    livro = encontrar_livro(livros, isbn)
    if livro is None:
        print("Livro não encontrado.")
        return livros
    if livro["status"] == "emprestado":
        print("Esse livro já está emprestado.")
        return livros
    livro["status"] = "emprestado"
    salvar_livros(livros)
    print("Empréstimo realizado com sucesso!")
    return livros

def devolver_livro(livros):
    """Registra a devolução de um livro."""
    print("\n===== DEVOLUÇÃO =====")
    isbn = input("Digite o ISBN do livro: ")
    livro = encontrar_livro(livros, isbn)
    if livro is None:
        print("Livro não encontrado.")
        return livros
    if livro["status"] == "disponível":
        print("Esse livro já está disponível.")
        return livros
    livro["status"] = "disponível"
    salvar_livros(livros)
    print("Devolução realizada com sucesso!")
    return livros

def listar_livros(livros):
    """Mostra todos os livros cadastrados."""
    print("\n===== LISTA DE LIVROS =====")
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("-" * 30)

def buscar_livro(livros):
    """Busca livros pelo título ou autor."""
    print("\n===== BUSCAR LIVRO =====")
    termo = input("Digite o título ou autor: ").lower()
    encontrados = []
    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            encontrados.append(livro)
    if len(encontrados) == 0:
        print("Nenhum livro encontrado.")
    else:
        print("\nLivros encontrados:")
        for livro in encontrados:
            print(
                f"{livro['titulo']} - {livro['autor']} "
                f"({livro['ano']}) - {livro['status']}"
            )
    return encontrados

def ordenar_livros(livros):
    """Ordena os livros por título, autor ou ano."""
    print("\n===== ORDENAR LIVROS =====")
    print("1 - Por título")
    print("2 - Por autor")
    print("3 - Por ano")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("Livros ordenados por título.")
    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("Livros ordenados por autor.")
    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])
        print("Livros ordenados por ano.")
    else:
        print("Opção inválida.")
        return livros
    salvar_livros(livros)
    return livros

def mostrar_menu():
    """Exibe o menu principal."""
    print("\n==============================")
    print("   SISTEMA DE BIBLIOTECA")
    print("==============================")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")

# Carrega os livros salvos quando o programa é iniciado.
livros = carregar_livros()
# Mantém o menu funcionando até o usuário escolher sair.
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        livros = cadastrar_livro(livros)
    elif opcao == "2":
        livros = emprestar_livro(livros)
    elif opcao == "3":
        livros = devolver_livro(livros)
    elif opcao == "4":
        listar_livros(livros)
    elif opcao == "5":
        buscar_livro(livros)
    elif opcao == "6":
        livros = ordenar_livros(livros)
    elif opcao == "7":
        salvar_livros(livros)
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
