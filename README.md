# Flask CI/CD Demo

![CI/CD Pipeline](https://github.com/hongqian-li/flask-cicd-demo/actions/workflows/ci-cd.yml/badge.svg)

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
- Docker for containerization
- GitHub Actions for CI/CD

## Running It Locally

### Without Docker:
```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app/main.py
```

### With Docker:
```bash
# Build and run
docker-compose up

# Or build the image manually
docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
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
# Run tests
pytest tests/ -v

# Run tests with coverage
pytest --cov=app tests/
```

The tests run automatically on every push through GitHub Actions.

## CI/CD Pipeline

Every push to the main branch triggers:
1. Automated testing with pytest
2. Docker image build
3. Container health verification

You can see the pipeline status in the badge at the top of this README.

## What I Learned

- How to structure a Flask app properly (separating app code from tests)
- Why health check endpoints matter for container orchestration
- Using environment variables for configuration (12-factor app principles)
- Why you need a proper WSGI server like Gunicorn for production
- Setting up CI/CD workflows with GitHub Actions
- Docker containerization best practices

## Project Structure
```
flask-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # CI/CD pipeline configuration
├── app/                  # Application code
│   ├── __init__.py
│   └── main.py
├── tests/                # Test files
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Local development setup
├── requirements.txt      # Python dependencies
└── .gitignore
```

## Future Improvements

Some ideas I'm considering:
- Add database integration (PostgreSQL)
- Implement user authentication
- Deploy to AWS/Azure using Terraform
- Add monitoring with Prometheus/Grafana
- Set up automated deployment to cloud platforms