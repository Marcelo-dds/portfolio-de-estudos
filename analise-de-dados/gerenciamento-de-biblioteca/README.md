# Sistema de Gestão de Biblioteca

Este projeto é um sistema simples de gestão de biblioteca desenvolvido em Python. Ele permite o cadastro de livros e usuários, além de gerenciar empréstimos e devoluções de livros. O sistema também pode gerar relatórios de livros disponíveis, livros emprestados e usuários cadastrados.

## Funcionalidades

1. **Cadastro de Livros**: Permite adicionar novos livros ao sistema.
2. **Cadastro de Usuários**: Permite adicionar novos usuários ao sistema.
3. **Empréstimo de Livros**: Permite registrar o empréstimo de livros aos usuários.
4. **Devolução de Livros**: Permite registrar a devolução de livros emprestados.
5. **Consulta de Livros por Título**: Permite consultar os detalhes de um livro específico pelo título.
6. **Consulta de Livros por Autor**: Permite consultar todos os livros de um autor específico.
7. **Consulta de Livros por Ano de Publicação**: Permite consultar todos os livros publicados em um ano específico.
8. **Relatório de Livros Disponíveis**: Gera um relatório com todos os livros que têm cópias disponíveis para empréstimo.
9. **Relatório de Livros Emprestados**: Gera um relatório com todos os livros que estão emprestados.
10. **Relatório de Usuários Cadastrados**: Gera um relatório com todos os usuários cadastrados no sistema.

## Estrutura do Código

### Classes

1. **Livro**: Representa um livro na biblioteca.
    - `titulo`: Título do livro.
    - `autor`: Autor do livro.
    - `ano_publicacao`: Ano de publicação do livro.
    - `num_copias`: Número de cópias disponíveis do livro.

2. **Usuario**: Representa um usuário da biblioteca.
    - `nome`: Nome do usuário.
    - `identificacao`: Identificação do usuário (ID).
    - `contato`: Contato do usuário (e-mail ou telefone).

### Listas

- **livros**: Lista que armazena os objetos do tipo `Livro`.
- **usuarios**: Lista que armazena os objetos do tipo `Usuario`.

### Funções

1. **cadastrar_livro(titulo, autor, ano_publicacao, num_copias)**: Cadastra um novo livro na lista de livros.
2. **cadastrar_usuario(nome, identificacao, contato)**: Cadastra um novo usuário na lista de usuários.
3. **emprestar_livro(titulo)**: Registra o empréstimo de um livro, diminuindo o número de cópias disponíveis.
4. **devolver_livro(titulo)**: Registra a devolução de um livro, aumentando o número de cópias disponíveis.
5. **consultar_livro_por_titulo(titulo)**: Consulta e exibe os detalhes de um livro específico pelo título.
6. **consultar_livro_por_autor(autor)**: Consulta e exibe os detalhes de todos os livros de um autor específico.
7. **consultar_livro_por_ano(ano)**: Consulta e exibe os detalhes de todos os livros publicados em um ano específico.
8. **relatorio_livros_disponiveis()**: Gera um relatório com todos os livros disponíveis para empréstimo.
9. **relatorio_livros_emprestados()**: Gera um relatório com todos os livros emprestados.
10. **relatorio_usuarios_cadastrados()**: Gera um relatório com todos os usuários cadastrados.

### Exemplo de Utilização

```python
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.num_copias = num_copias

class Usuario:
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

livros = []
usuarios = []

def cadastrar_livro(titulo, autor, ano_publicacao, num_copias):
    livro = Livro(titulo, autor, ano_publicacao, num_copias)
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

def cadastrar_usuario(nome, identificacao, contato):
    usuario = Usuario(nome, identificacao, contato)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def emprestar_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            if livro.num_copias > 0:
                livro.num_copias -= 1
                print("Livro emprestado com sucesso!")
                return
            else:
                print("Livro não disponível para empréstimo.")
                return
    print("Livro não encontrado.")

def devolver_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            livro.num_copias += 1
            print("Livro devolvido com sucesso!")
            return
    print("Livro não encontrado.")

def consultar_livro_por_titulo(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
            return
    print("Livro não encontrado.")

def consultar_livro_por_autor(autor):
    for livro in livros:
        if livro.autor.lower() == autor.lower():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
    print("Nenhum livro encontrado para esse autor.")

def consultar_livro_por_ano(ano):
    for livro in livros:
        if livro.ano_publicacao == ano:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
    print("Nenhum livro encontrado para esse ano.")

# Função para gerar relatório de livros disponíveis
def relatorio_livros_disponiveis():
    print("Livros disponíveis:")
    for livro in livros:
        if livro.num_copias > 0:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")

# Função para gerar relatório de livros emprestados
def relatorio_livros_emprestados():
    print("Livros emprestados:")
    for livro in livros:
        if livro.num_copias < livro.total_copias:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")

# Função para gerar relatório de usuários cadastrados
def relatorio_usuarios_cadastrados():
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario.nome}, Identificação: {usuario.identificacao}, Contato: {usuario.contato}")

# Exemplo de utilização das funções
cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, 5)
cadastrar_livro("Harry Potter", "J.K. Rowling", 1997, 3)
cadastrar_usuario("João", 12345, "joao@email.com")

emprestar_livro("Dom Casmurro")
consultar_livro_por_titulo("Dom Casmurro")
relatorio_livros_disponiveis()
