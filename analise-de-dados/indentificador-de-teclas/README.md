# Sistema de Identificação de Teclas

Projeto desenvolvido para o portfólio da matéria de Linguagem de Programação da graduação em Análise de Dados. O objetivo é criar um sistema simples que identifica as teclas que o usuário clica.

## Descrição

Este script foi criado para identificar e registrar as teclas pressionadas pelo usuário. Ele monitora as entradas do teclado e grava cada tecla pressionada em um arquivo de log.

## Pré-requisitos

Antes de rodar o script, você vai precisar de:

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório para a sua máquina:
    ```bash
    git clone https://github.com/Marcelo-dds/portfolio-de-estudos.git
    ```
2. Entre no diretório do projeto:
    ```bash
    cd sistema-identificacao-teclas
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Rodando o Script

Para rodar o script, siga estes passos:

1. Abra o terminal e vá para o diretório do projeto:
    ```bash
    cd sistema-identificacao-teclas
    ```
2. Execute o script:
    ```bash
    python detector-de-teclas.py
    ```

### Parâmetros de Entrada

O script aceita os seguintes parâmetros:

- `-o` ou `--output`: Caminho para o arquivo de saída. Exemplo:
    ```bash
    python detector-de-teclas.py -o logs/teclas_pressionadas.txt
    ```

### Exemplo de Uso

Aqui está um exemplo de como usar o script:

```bash
python detector-de-teclas.py -o logs/teclas_pressionadas.txt
