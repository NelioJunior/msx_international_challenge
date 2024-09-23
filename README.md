# msx_international_challenge - API de Gerenciamento de Veículos

Esta API RESTful permite o gerenciamento de uma frota de veículos, oferecendo operações CRUD (Create, Read, Update, Delete) para informações de veículos.

## Índice

- [msx\_international\_challenge - API de Gerenciamento de Veículos](#msx_international_challenge---api-de-gerenciamento-de-veículos)
  - [Índice](#índice)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Configuração do Ambiente](#configuração-do-ambiente)
  - [Executando a Aplicação](#executando-a-aplicação)
  - [Autenticação](#autenticação)
  - [Endpoints](#endpoints)
    - [GET /veiculos](#get-veiculos)
    - [POST /veiculos](#post-veiculos)
    - [GET /veiculos/](#get-veiculos-1)
    - [PUT /veiculos/](#put-veiculos)
    - [DELETE /veiculos/](#delete-veiculos)
  - [Exemplos de Uso](#exemplos-de-uso)
    - [Listar todos os veículos](#listar-todos-os-veículos)
    - [Criar um novo veículo](#criar-um-novo-veículo)
    - [Obter detalhes de um veículo](#obter-detalhes-de-um-veículo)
    - [Atualizar o status de um veículo](#atualizar-o-status-de-um-veículo)
    - [Excluir um veículo](#excluir-um-veículo)
  - [Executando os Testes](#executando-os-testes)
  - [Testando com Postman](#testando-com-postman)
    - [Configuração Inicial](#configuração-inicial)
    - [Configurando a Autenticação](#configurando-a-autenticação)
    - [Criando Requisições](#criando-requisições)
      - [1. Listar Veículos (GET)](#1-listar-veículos-get)
      - [2. Criar Veículo (POST)](#2-criar-veículo-post)
      - [3. Obter Detalhes do Veículo (GET)](#3-obter-detalhes-do-veículo-get)
      - [4. Atualizar Status do Veículo (PUT)](#4-atualizar-status-do-veículo-put)
      - [5. Excluir Veículo (DELETE)](#5-excluir-veículo-delete)
    - [Executando os Testes](#executando-os-testes-1)
    - [Dicas para Testes no Postman](#dicas-para-testes-no-postman)
    - [Tratamento de Erros](#tratamento-de-erros)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Possíveis Melhorias Futuras](#possíveis-melhorias-futuras)

## Tecnologias Utilizadas

- Python 3.8+
- Flask
- Flask-HTTPAuth

## Configuração do Ambiente

1. Clone o repositório:
   ```
   git clone git@github.com:NelioJunior/msx_international_challenge.git
   cd /msx_international_challenge
   ```

2. Crie e ative um ambiente virtual no Linux:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```
   API_USERNAME=admin
   API_PASSWORD=MSX123
   ```

## Executando a Aplicação

Para iniciar a aplicação, execute:

```
python app.py
```

A API estará disponível em `http://localhost:5000`.

## Autenticação

A API utiliza autenticação básica HTTP. Para todas as requisições, você precisará fornecer um nome de usuário e senha válidos. As credenciais padrão são:

- Username: admin
- Password: MSX123

## Endpoints

### GET /veiculos

Retorna a lista de todos os veículos.

**Resposta de Sucesso:**
- Código: 200
- Conteúdo: Array de objetos de veículo

### POST /veiculos

Cria um novo veículo.

**Parâmetros da Requisição:**
```json
{
  "placa": "ABC1234",
  "marca": "Honda",
  "fabricante": "Honda",
  "cor": "Prata",
  "tipo": "Sedan",
  "combustivel": "Gasolina",
  "status": "CONNECTADO"
}
```

**Resposta de Sucesso:**
- Código: 201
- Conteúdo: Objeto do veículo criado

### GET /veiculos/<placa>

Retorna os detalhes de um veículo específico.

**Resposta de Sucesso:**
- Código: 200
- Conteúdo: Objeto do veículo

**Resposta de Erro:**
- Código: 404
- Conteúdo: { "error": "Veículo não encontrado" }

### PUT /veiculos/<placa>

Atualiza o status de um veículo.

**Parâmetros da Requisição:**
```json
{
  "status": "CONNECTADO"
}
```

**Resposta de Sucesso:**
- Código: 200
- Conteúdo: Objeto do veículo atualizado

**Resposta de Erro:**
- Código: 400
- Conteúdo: { "error": "Status inválido" }

### DELETE /veiculos/<placa>

Exclui um veículo.

**Resposta de Sucesso:**
- Código: 200
- Conteúdo: { "result": true }

## Exemplos de Uso

### Listar todos os veículos

```bash
curl -u admin:MSX123 http://localhost:5000/veiculos
```

### Criar um novo veículo

```bash
curl -u admin:MSX123 -X POST -H "Content-Type: application/json" -d '{"placa":"DEF5678","marca":"Toyota","fabricante":"Toyota","cor":"Azul","tipo":"SUV","combustivel":"Híbrido"}' http://localhost:5000/veiculos
```

### Obter detalhes de um veículo

```bash
curl -u admin:MSX123 http://localhost:5000/veiculos/ABC1234
```

### Atualizar o status de um veículo

```bash
curl -u admin:MSX123 -X PUT -H "Content-Type: application/json" -d '{"status":"CONNECTADO"}' http://localhost:5000/veiculos/ABC1234
```

### Excluir um veículo

```bash
curl -u admin:MSX123 -X DELETE http://localhost:5000/veiculos/ABC1234
```

## Executando os Testes

Para executar os testes unitários, use o seguinte comando:

```bash
python -m unittest test_app.py
```

## Testando com Postman

O Postman é uma ferramenta popular para testar APIs. Aqui estão as instruções para configurar e usar o Postman para testar nossa API de Gerenciamento de Veículos:

### Configuração Inicial

1. Baixe e instale o Postman a partir do [site oficial](https://www.postman.com/downloads/).
2. Abra o Postman e crie uma nova coleção chamada "API de Gerenciamento de Veículos".

### Configurando a Autenticação

1. Clique na coleção "API de Gerenciamento de Veículos".
2. Vá para a aba "Authorization".
3. Selecione o tipo "Basic Auth".
4. Insira o username e password (por padrão, admin e MSX123).

### Criando Requisições

Crie uma nova requisição para cada endpoint da API:

#### 1. Listar Veículos (GET)

- Método: GET
- URL: `http://localhost:5000/veiculos`

#### 2. Criar Veículo (POST)

- Método: POST
- URL: `http://localhost:5000/veiculos`
- Headers: 
  - Key: Content-Type
  - Value: application/json
- Body (raw JSON):
  ```json
  {
    "placa": "XYZ9876",
    "marca": "Tesla",
    "fabricante": "Tesla",
    "cor": "Prata",
    "tipo": "Sedan",
    "combustivel": "Elétrico",
    "status": "CONNECTADO"
  }
  ```

#### 3. Obter Detalhes do Veículo (GET)

- Método: GET
- URL: `http://localhost:5000/veiculos/XYZ9876`

#### 4. Atualizar Status do Veículo (PUT)

- Método: PUT
- URL: `http://localhost:5000/veiculos/XYZ9876`
- Headers: 
  - Key: Content-Type
  - Value: application/json
- Body (raw JSON):
  ```json
  {
    "status": "CONNECTADO"
  }
  ```

#### 5. Excluir Veículo (DELETE)

- Método: DELETE
- URL: `http://localhost:5000/veiculos/XYZ9876`

### Executando os Testes

1. Certifique-se de que a API está rodando localmente (`python app.py`).
2. No Postman, selecione a requisição que deseja testar.
3. Clique no botão "Send" para enviar a requisição.
4. Observe a resposta na seção inferior da janela do Postman.

### Dicas para Testes no Postman

- Use a funcionalidade "Environment" do Postman para armazenar variáveis como a URL base e as credenciais de autenticação.
- Utilize a aba "Tests" em cada requisição para adicionar testes automatizados, como verificação de código de status e formato de resposta.
- Use a funcionalidade "Runner" do Postman para executar uma série de testes em sequência.

### Tratamento de Erros

Teste cenários de erro, como:
- Tentar criar um veículo com dados inválidos
- Tentar atualizar ou excluir um veículo que não existe
- Acessar a API sem autenticação ou com credenciais inválidas

Observe as respostas de erro e certifique-se de que estão de acordo com a documentação da API.

## Estrutura do Projeto

```
projeto/
├── app.py
├── veiculos.json
├── test_app.py
├── requirements.txt
├── .env
└── README.md
```

- `app.py`: Contém a lógica principal da aplicação.
- `veiculos.json`: Arquivo JSON usado como banco de dados simulado.
- `test_app.py`: Contém os testes unitários.
- `requirements.txt`: Lista todas as dependências do projeto.
- `.env`: Armazena variáveis de ambiente (não deve ser versionado em um cenário real).
- `README.md`: Este arquivo, contendo a documentação do projeto.








## Possíveis Melhorias Futuras

1. **Banco de Dados**: Substituir o arquivo JSON por um banco de dados real (ex: SQLite, PostgreSQL).
2. **Paginação**: Implementar paginação para o endpoint GET /veiculos.
3. **Rate Limiting**: Adicionar limitação de taxa para proteger a API contra uso excessivo.
4. **CORS**: Configurar Cross-Origin Resource Sharing para permitir o uso da API por aplicações web em diferentes domínios.
5. **Dockerização**: Criar um Dockerfile para facilitar a implantação e garantir consistência entre ambientes.
