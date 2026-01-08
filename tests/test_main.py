import pytest
import json
from app.main import app

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint returns healthy status"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'UP'

def test_get_tasks(client):
    """Test retrieving all tasks"""
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)

def test_get_single_task(client):
    """Test retrieving a specific task by ID"""
    response = client.get('/api/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1

def test_get_nonexistent_task(client):
    """Test retrieving a non-existent task returns 404"""
    response = client.get('/api/tasks/999')
    assert response.status_code == 404

def test_create_task(client):
    """Test creating a new task"""
    new_task = {"title": "Test Task"}
    response = client.post(
        '/api/tasks',
        data=json.dumps(new_task),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Task'
    assert 'id' in data

def test_create_task_without_title(client):
    """Test that creating a task without a title returns 400"""
    response = client.post(
        '/api/tasks',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400