# Tasks Flask CRUD

A simple REST API for task management, built with **Flask**. The project implements the four basic CRUD operations — create, list, update, and delete tasks — using an in-memory list for storage.

## ✨ Features

- ✅ Create a new task
- 📋 List all tasks
- 🔍 Find a specific task by `id`
- ✏️ Update an existing task
- 🗑️ Delete a task

## 🛠️ Tech Stack

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Cors](https://flask-cors.readthedocs.io/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)

## 📁 Project Structure

```
tasks-flask-crud/
├── models/
│   └── task.py          # Task model/class definition
├── app.py                # API routes and main logic
├── requirements.txt       # Project dependencies
└── .gitignore
```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/saulobdsena/tasks-flask-crud.git
   cd tasks-flask-crud
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

The API will be available at `http://127.0.0.1:5000`, running in debug mode.

## 📡 API Endpoints

| Method   | Route            | Description                        |
|----------|------------------|--------------------------------------|
| `POST`   | `/tasks`         | Creates a new task                   |
| `GET`    | `/tasks`         | Lists all tasks                      |
| `GET`    | `/tasks/<id>`    | Finds a task by `id`                 |
| `PUT`    | `/tasks/<id>`    | Updates an existing task             |
| `DELETE` | `/tasks/<id>`    | Deletes a task                       |

### Example payload (POST/PUT)

```json
{
  "title": "Study Flask",
  "description": "Review routes and HTTP methods",
  "completed": false
}
```

### Example response (GET /tasks)

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Flask",
      "description": "Review routes and HTTP methods",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

## ⚠️ Note

Tasks are currently stored in an in-memory list (`task_list`), which means **all data is lost every time the server restarts**. The project already includes `Flask-SQLAlchemy` among its dependencies, suggesting future persistence with a database.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements such as:

- Database persistence (SQLite/PostgreSQL via SQLAlchemy)
- Input data validation
- Automated tests

## 📄 License

This project is available for study purposes. Add a license (e.g. MIT) if you'd like to formalize its use.

## 👤 Author

Developed by [saulobdsena](https://github.com/saulobdsena).