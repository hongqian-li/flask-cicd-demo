from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# Simple task management API for demonstration
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Learn GitHub Actions", "completed": False}
]

@app.route('/')
def home():
    """Health check endpoint - validates if the service is running"""
    return jsonify({
        "status": "healthy",
        "service": "Flask CI/CD Demo",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({"tasks": tasks, "count": len(tasks)})

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task by ID"""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": max([t["id"] for t in tasks]) + 1 if tasks else 1,
        "title": data["title"],
        "completed": data.get("completed", False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/health')
def health():
    """Kubernetes/Docker style health check endpoint"""
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)