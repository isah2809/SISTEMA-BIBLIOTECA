# Sistema de Gerenciamento de Biblioteca

Sistema desenvolvido em Python para controlar o acervo de uma biblioteca, permitindo cadastro, empréstimo, devolução, listagem, busca e ordenação de livros.

## Como executar o programa

1. Certifique-se de ter o Python 3 instalado na máquina
2. Abra o terminal na pasta do projeto
3. Execute o comando:
   ```
   python main.py
   ```
4. Use o menu interativo para navegar pelas opções

## Principais funcionalidades

1. **Cadastrar livro** - Adiciona um novo livro ao acervo (título, autor, ano, ISBN e status)
2. **Emprestar livro** - Marca um livro como "emprestado" pelo ISBN
3. **Devolver livro** - Marca um livro como "disponível" novamente
4. **Listar livros** - Mostra todos os livros cadastrados com seus respectivos status
5. **Buscar livro** - Pesquisa por título ou autor
6. **Ordenar livros** - Organiza a lista por título, autor ou ano de publicação

## Requisitos técnicos aplicados

Aqui estão os requisitos técnicos obrigatórios e onde foram aplicados no código:

- **Menu principal com if/elif/else** → Na função `main()`, linhas 225 a 249, que controlam as 7 opções do menu
- **Estrutura de repetição while** → Na função `main()`, linha 220, que mantém o menu ativo até o usuário escolher "sair" (opção 7)
- **No mínimo 3 funções próprias com parâmetros e retorno** → Foram criadas 9 funções:
  - `carregar_livros()` → sem parâmetro, retorna lista de livros
  - `salvar_livros(livros)` → recebe lista, salva em arquivo (sem retorno)
  - `cadastrar_livro(livros)` → recebe lista, retorna lista atualizada
  - `encontrar_livro(livros, isbn)` → recebe lista e ISBN, retorna livro ou None
  - `emprestar_livro(livros)` → recebe lista, retorna lista atualizada
  - `devolver_livro(livros)` → recebe lista, retorna lista atualizada
  - `listar_livros(livros)` → recebe lista, imprime na tela (sem retorno)
  - `buscar_livro(livros)` → recebe lista, retorna lista de encontrados
  - `ordenar_livros(livros)` → recebe lista, retorna lista ordenada
- **Lista de dicionários em memória** → Cada livro é um dicionário com chaves: `titulo`, `autor`, `ano`, `isbn`, `status`. Todos ficam armazenados na lista `livros`.
- **Persistência de dados em arquivo CSV** → Leitura na função `carregar_livros()` (linhas 6 a 22) e escrita na função `salvar_livros()` (linhas 25 a 33), usando a biblioteca `csv` padrão do Python.
- **Apenas biblioteca padrão** → Foram usadas apenas `csv` (leitura/escrita) e nenhum pacote externo foi instalado.

## Estrutura do projeto

```
sistema-biblioteca/
├── main.py      (arquivo principal com todo o sistema)
├── livros.csv   (arquivo onde os livros são salvos)
└── README.md    (este arquivo)
```
