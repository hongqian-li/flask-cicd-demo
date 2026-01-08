# Flask CI/CD Demo

A simple Flask REST API that I built to practice modern DevOps workflows. This project is part of my learning journey in cloud engineering and CI/CD automation.

## What This Project Does

This is a basic task management API that lets you create and retrieve tasks. Nothing fancy - the focus here is on the development workflow rather than complex features.

**Why I built this:**
- Practice writing production-ready Python code
- Learn Docker containerization
- Set up automated testing and CI/CD pipelines
- Build something I can actually show in interviews

## Tech Stack

- Flask (because it's lightweight and good for microservices)
- pytest for testing
- Gunicorn as the production server
- Docker (in progress)
- GitHub Actions for CI/CD (coming next)

## Running It Locally
```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app/main.py
```

Visit `http://localhost:5000` and you should see a health check response.

## API Endpoints

- `GET /` - Health check
- `GET /health` - Simple status check (for Docker/K8s)
- `GET /api/tasks` - List all tasks
- `GET /api/tasks/<id>` - Get specific task
- `POST /api/tasks` - Create a new task

## Testing
```bash
pytest tests/ -v
```

I wrote tests for the main endpoints including error cases (404s, 400s, etc). The tests run automatically in the CI pipeline.

## What I Learned

- How to structure a Flask app properly (separating app code from tests)
- Why health check endpoints matter for container orchestration
- Using environment variables for configuration (12-factor app principles)
- Why you need a proper WSGI server like Gunicorn for production

## Next Steps

I'm currently adding:
- Dockerfile and docker-compose setup
- GitHub Actions workflow for automated testing
- Deployment pipeline

## Project Structure
```
flask-cicd-demo/
├── app/              # Application code
├── tests/            # Test files
├── requirements.txt
└── .gitignore
```