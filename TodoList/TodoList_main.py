from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,  request, jsonify
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
CORS(app)
# MongoDB connection
mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['TodoList']
collection = db['tasks']

# Function to add a new task with an initialized date
# Function to view all tasks
@app.route('/tasks', methods=['GET'])
def get_task():
    tasks = list(collection.find())
    for task in tasks:
        # print({
        #     "ID": str(task['_id']),
        #     "Description": task['description'],
        #     "Due Date": task['due_date'],
        #     "Priority": task['priority'],
        #     "Completed": task['completed'],
        #     "Created At": task['created_at']
        # })
        for task in tasks:
            task['_id'] = str(task['_id'])
    return jsonify(tasks)


@app.route('/tasks/addTask', methods=['POST'])
def add_task():
    task_data = request.json
    description = task_data['description']
    due_date = task_data['due_date']
    priority = task_data.get('priority', 'Normal')  # Default to 'Normal' if not provided
    
    # Add task to MongoDB
    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    result = collection.insert_one(task)
    
    return jsonify({"message": "Task added", "task_id": str(result.inserted_id)})

def add_task_2(description,due_date,priority='Normal'):
      # Default to 'Normal' if not provided
    
    # Add task to MongoDB
    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    result = collection.insert_one(task)
    
    return True

# Function to delete a task by its ID
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = collection.delete_one({"_id": ObjectId(task_id)})
    print(f"Task deleted: {result.deleted_count}")
    return jsonify({"message": "Task deleted", "deleted_count": result.deleted_count})

# Function to update a task's details
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id, description=None, due_date=None, priority=None, completed=None):
    new_values = {}
    if description:
        new_values["description"] = description
    if due_date:
        new_values["due_date"] = due_date
    if priority:
        new_values["priority"] = priority
    if completed is not None:  # Allows setting 'completed' to True or False
        new_values["completed"] = completed
    result = collection.update_one({"_id": ObjectId(task_id)}, {"$set": new_values})
    print(f"Task updated: {result.modified_count}")
    return jsonify({"message": "Task updated", "modified_count": result.modified_count})

# Function to mark a task as completed
@app.route('/tasks/<task_id>/complete', methods=['PUT'])
def mark_completed(task_id):
    result = collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
    print(f"Task completed: {result.modified_count}")
    return jsonify({"message": "Task marked as completed", "modified_count": result.modified_count})

# # Example usage
# add_task("Complete AI project", "2024-10-15", "High")
# add_task("Submit AI project", "2024-10-20", "Normal")
# view_task()
# delete_task("670510fda674f75aa2a0e7ec")
# view_task()
# update_task("670510fda674f75aa2a0e7ed", priority="High")
# view_task()
# mark_completed("670510fda674f75aa2a0e7ed")
# view_task()
if __name__ == '__main__':
    app.run(debug=True)