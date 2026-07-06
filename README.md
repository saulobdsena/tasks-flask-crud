# Tasks Flask CRUD

API REST desenvolvida com **Python** e **Flask** para gerenciamento de tarefas.

O projeto implementa as principais operações de um CRUD:

* Criar uma tarefa;
* Listar todas as tarefas;
* Buscar uma tarefa pelo ID;
* Atualizar uma tarefa;
* Excluir uma tarefa.

> Este projeto foi desenvolvido para praticar a criação de APIs REST, rotas HTTP, manipulação de JSON e organização de código com Flask.

## Tecnologias utilizadas

* Python 3
* Flask
* Werkzeug
* Requests
* Pytest

## Estrutura do projeto

```text
tasks-flask-crud/
├── models/
│   └── task.py
├── app.py
├── requirements.txt
└── README.md
```

### Descrição dos arquivos

* `app.py`: inicialização da aplicação e definição das rotas da API.
* `models/task.py`: classe responsável por representar uma tarefa.
* `requirements.txt`: dependências necessárias para executar o projeto.

## Modelo de tarefa

Cada tarefa possui os seguintes campos:

| Campo         | Tipo    | Descrição                        |
| ------------- | ------- | -------------------------------- |
| `id`          | Integer | Identificador único da tarefa    |
| `title`       | String  | Título da tarefa                 |
| `description` | String  | Descrição da tarefa              |
| `completed`   | Boolean | Indica se a tarefa foi concluída |

Exemplo:

```json
{
  "id": 1,
  "title": "Estudar Flask",
  "description": "Praticar a criação de APIs REST",
  "completed": false
}
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/saulobdsena/tasks-flask-crud.git
```

Entre na pasta do projeto:

```bash
cd tasks-flask-crud
```

### 2. Criar um ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints da API

| Método   | Endpoint      | Descrição                 |
| -------- | ------------- | ------------------------- |
| `POST`   | `/tasks`      | Criar uma nova tarefa     |
| `GET`    | `/tasks`      | Listar todas as tarefas   |
| `GET`    | `/tasks/<id>` | Buscar uma tarefa pelo ID |
| `PUT`    | `/tasks/<id>` | Atualizar uma tarefa      |
| `DELETE` | `/tasks/<id>` | Excluir uma tarefa        |

## Criar uma tarefa

### Requisição

```http
POST /tasks
Content-Type: application/json
```

```json
{
  "title": "Estudar Flask",
  "description": "Praticar a criação de rotas",
  "completed": false
}
```

Exemplo utilizando `curl`:

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar Flask",
    "description": "Praticar a criação de rotas",
    "completed": false
  }'
```

### Resposta

```json
{
  "message": "New task has created",
  "id": 1
}
```

## Listar todas as tarefas

### Requisição

```http
GET /tasks
```

Exemplo utilizando `curl`:

```bash
curl http://127.0.0.1:5000/tasks
```

### Resposta

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Flask",
      "description": "Praticar a criação de rotas",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

Quando não existem tarefas cadastradas:

```json
{
  "tasks": [],
  "total_tasks": 0
}
```

## Buscar uma tarefa pelo ID

### Requisição

```http
GET /tasks/1
```

Exemplo utilizando `curl`:

```bash
curl http://127.0.0.1:5000/tasks/1
```

### Resposta de sucesso

```json
{
  "id": 1,
  "title": "Estudar Flask",
  "description": "Praticar a criação de rotas",
  "completed": false
}
```

### Tarefa não encontrada

Status HTTP:

```text
404 Not Found
```

Resposta:

```json
{
  "message": "Task doesnt exist"
}
```

## Atualizar uma tarefa

A atualização exige o envio dos campos `title`, `description` e `completed`.

### Requisição

```http
PUT /tasks/1
Content-Type: application/json
```

```json
{
  "title": "Estudar Flask e APIs",
  "description": "Praticar operações CRUD",
  "completed": true
}
```

Exemplo utilizando `curl`:

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar Flask e APIs",
    "description": "Praticar operações CRUD",
    "completed": true
  }'
```

### Resposta de sucesso

```json
{
  "message": "Task updated!"
}
```

### Tarefa não encontrada

Status HTTP:

```text
404 Not Found
```

Resposta:

```json
{
  "message": "Error: task not found"
}
```

## Excluir uma tarefa

### Requisição

```http
DELETE /tasks/1
```

Exemplo utilizando `curl`:

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

### Resposta de sucesso

```json
{
  "message": "Task removed!"
}
```

### Tarefa não encontrada

Status HTTP:

```text
404 Not Found
```

Resposta:

```json
{
  "message": "Error: task not found"
}
```

## Armazenamento dos dados

Atualmente, as tarefas são armazenadas em uma lista em memória:

```python
task_list = []
```

Isso significa que todos os dados cadastrados são apagados quando a aplicação é encerrada ou reiniciada.

## Possíveis melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* Persistência de dados com SQLite ou PostgreSQL;
* Integração com Flask-SQLAlchemy;
* Validação dos dados recebidos;
* Tratamento para requisições sem JSON;
* Retorno do status `201 Created` na criação de tarefas;
* Atualização parcial de tarefas com `PATCH`;
* Testes automatizados com Pytest;
* Documentação com Swagger/OpenAPI;
* Paginação da listagem de tarefas;
* Autenticação e autorização de usuários;
* Containerização com Docker.

## Autor

Desenvolvido por [Saulo Sena](https://github.com/saulobdsena).

Projeto criado para fins de estudo e prática de desenvolvimento de APIs com Flask.
