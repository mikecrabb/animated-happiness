from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# In-memory storage for tasks
tasks = {}

class Task(Resource):
    def get(self, task_id):
        """Retrieve a task by ID"""
        if task_id in tasks:
            return tasks[task_id], 200
        return {"message": "Task not found"}, 404

    def post(self, task_id):
        """Create a new task"""
        if task_id in tasks:
            return {"message": "Task already exists"}, 400

        data = request.get_json()
        if not data or "task" not in data:
            return {"message": "Missing 'task' field in request body"}, 400

        tasks[task_id] = {"task": data["task"], "completed": False}
        return tasks[task_id], 201

    def put(self, task_id):
        """Update an existing task"""
        if task_id not in tasks:
            return {"message": "Task not found"}, 404

        data = request.get_json()
        if not data or "task" not in data:
            return {"message": "Missing 'task' field in request body"}, 400

        tasks[task_id]["task"] = data["task"]
        if "completed" in data:
            tasks[task_id]["completed"] = data["completed"]

        return tasks[task_id], 200

    def delete(self, task_id):
        """Delete a task by ID"""
        if task_id in tasks:
            del tasks[task_id]
            return {"message": "Task deleted"}, 200
        return {"message": "Task not found"}, 404

api.add_resource(Task, "/task/<int:task_id>")

if __name__ == '__main__':
    app.run(debug=True)
