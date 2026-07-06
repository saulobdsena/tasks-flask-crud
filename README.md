# Tasks Flask CRUD

A REST API built with **Python** and **Flask** for task management.

The project implements the main CRUD operations:

* Create a task;
* List all tasks;
* Find a task by ID;
* Update a task;
* Delete a task.

> This project was developed to practice REST API development, HTTP routes, JSON handling, and code organization with Flask.

## Technologies

* Python 3
* Flask
* Werkzeug
* Requests
* Pytest

## Project Structure

```text
tasks-flask-crud/
├── models/
│   └── task.py
├── app.py
├── requirements.txt
└── README.md
```

### File Description

* `app.py`: initializes the application and defines the API routes.
* `models/task.py`: contains the class used to represent a task.
* `requirements.txt`: contains the dependencies required to run the project.

## Task Model

Each task contains the following fields:

| Field         | Type    | Description                                   |
| ------------- | ------- | --------------------------------------------- |
| `id`          | Integer | Unique task identifier                        |
| `title`       | String  | Task title                                    |
| `description` | String  | Task description                              |
| `completed`   | Boolean | Indicates whether the task has been completed |

Example:

```json
{
  "id": 1,
  "title": "Study Flask",
  "description": "Practice REST API development",
  "completed": false
}
```

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/saulobdsena/tasks-flask-crud.git
```

Navigate to the project directory:

```bash
cd tasks-flask-crud
```

### 2. Create a virtual environment

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method   | Endpoint      | Description              |
| -------- | ------------- | ------------------------ |
| `POST`   | `/tasks`      | Creates a new task       |
| `GET`    | `/tasks`      | Lists all tasks          |
| `GET`    | `/tasks/<id>` | Finds a task by ID       |
| `PUT`    | `/tasks/<id>` | Updates an existing task |
| `DELETE` | `/tasks/<id>` | Deletes a task           |

## Create a Task

### Request

```http
POST /tasks
Content-Type: application/json
```

```json
{
  "title": "Study Flask",
  "description": "Practice creating API routes",
  "completed": false
}
```

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Study Flask",
    "description": "Practice creating API routes",
    "completed": false
  }'
```

### Response

```json
{
  "message": "New task has created",
  "id": 1
}
```

## List All Tasks

### Request

```http
GET /tasks
```

Example using `curl`:

```bash
curl http://127.0.0.1:5000/tasks
```

### Response

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Flask",
      "description": "Practice creating API routes",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

When no tasks have been created:

```json
{
  "tasks": [],
  "total_tasks": 0
}
```

## Find a Task by ID

### Request

```http
GET /tasks/1
```

Example using `curl`:

```bash
curl http://127.0.0.1:5000/tasks/1
```

### Successful Response

```json
{
  "id": 1,
  "title": "Study Flask",
  "description": "Practice creating API routes",
  "completed": false
}
```

### Task Not Found

HTTP status:

```text
404 Not Found
```

Response:

```json
{
  "message": "Task doesnt exist"
}
```

## Update a Task

The update request requires the `title`, `description`, and `completed` fields.

### Request

```http
PUT /tasks/1
Content-Type: application/json
```

```json
{
  "title": "Study Flask and APIs",
  "description": "Practice CRUD operations",
  "completed": true
}
```

Example using `curl`:

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Study Flask and APIs",
    "description": "Practice CRUD operations",
    "completed": true
  }'
```

### Successful Response

```json
{
  "message": "Task updated!"
}
```

### Task Not Found

HTTP status:

```text
404 Not Found
```

Response:

```json
{
  "message": "Error: task not found"
}
```

## Delete a Task

### Request

```http
DELETE /tasks/1
```

Example using `curl`:

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

### Successful Response

```json
{
  "message": "Task removed!"
}
```

### Task Not Found

HTTP status:

```text
404 Not Found
```

Response:

```json
{
  "message": "Error: task not found"
}
```

## Data Storage

Tasks are currently stored in an in-memory list:

```python
task_list = []
```

This means that all registered tasks are deleted whenever the application is stopped or restarted.

## Future Improvements

Possible improvements for the project include:

* Database persistence with SQLite or PostgreSQL;
* Flask-SQLAlchemy integration;
* Request data validation;
* Error handling for requests without JSON;
* Return the `201 Created` status when creating tasks;
* Partial task updates using `PATCH`;
* Automated tests with Pytest;
* Swagger/OpenAPI documentation;
* Task list pagination;
* User authentication and authorization;
* Docker support.

## Author

Developed by [Saulo Sena](https://github.com/saulobdsena).

This project was created for learning and practicing REST API development with Flask.
