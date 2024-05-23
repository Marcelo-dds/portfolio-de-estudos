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
