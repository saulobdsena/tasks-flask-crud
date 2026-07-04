from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

#CRUD
task_list = []
task_id_control = 1

#Create task
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""),completed=data.get("completed"))
    task_id_control += 1 
    task_list.append(new_task)
    print(data)

    return jsonify({"message": "New task has created"})

#Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    
    task_view = [task.to_dict() for task in task_list]

    output = {

        "tasks": task_view, 
        "total_tasks": len(task_view)
    }

    return jsonify(output)

#Get task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):

    for t in task_list:
        if t.id == id:
            return jsonify(t.to_dict())
            
    
    return jsonify ({"message": "Task doesnt exist"}), 404


#Update task
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None 
    
    for t in task_list:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Error: task not found"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({"message": "Task updated!"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):

    task = None
    for t in task_list:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Error: task not found"}), 404
    
    else:
        task_list.remove(task)
        return jsonify({"message": "Task removed!"})

if __name__ == "__main__":
    app.run(debug=True)