from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

#CRUD
task_list = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""),completed=data.get("completed"))
    task_id_control += 1 
    task_list.append(new_task)
    print(data)

    return jsonify({"message": "New task has created"})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    
    task_view = [task.to_dict() for task in task_list]

    output = {

        "tasks": task_list, 
        "total_tasks": 0
    }

    return jsonify(output)



if __name__ == "__main__":
    app.run(debug=True)