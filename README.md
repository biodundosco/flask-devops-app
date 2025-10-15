# Flask DevOps CI/CD Pipeline Project

## Project Overview
A complete DevOps pipeline demonstrating automated containerized application deployment using Docker, GitHub Actions, and AWS EC2.

## Live Demo
🌐 **Application URL:** http://34.207.59.113:5000

## Technologies Used
- **Backend:** Python Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Container Registry:** Docker Hub
- **Cloud Provider:** AWS EC2
- **Version Control:** Git/GitHub

## Architecture
```
GitHub Repository → GitHub Actions → Docker Hub → AWS EC2 → Live Application
```

## Features
- ✅ Automated CI/CD pipeline
- ✅ Containerized deployment
- ✅ Health check endpoint (`/health`)
- ✅ Automatic deployment on git push
- ✅ Version tracking
- ✅ Zero-downtime deployments

## Project Structure
```
flask-devops-app/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── .dockerignore            # Docker ignore rules
├── .github/
│   └── workflows/
│       └── deploy.yml       # CI/CD pipeline
└── README.md                # Documentation
```

## Setup Instructions

### Prerequisites
- AWS Account
- GitHub Account
- Docker Hub Account
- Docker installed locally

### Local Development
```bash
# Create a flask-devops-app directory 
mkdir flask-devops-app
cd flask-devops-app
git init

cd flask-devops-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Docker Build & Run
```bash
# Build image
docker build -t flask-devops-app:latest .

# Run container
docker run -d -p 5000:5000 flask-devops-app:latest
```

## CI/CD Pipeline

The pipeline automatically:
1. Triggers on push to main branch
2. Builds Docker image
3. Pushes to Docker Hub
4. Deploys to AWS EC2
5. Runs the application

### Required GitHub Secrets
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `EC2_HOST`
- `EC2_USERNAME`
- `EC2_SSH_KEY`

## Challenges Faced & Solutions

### Challenge 1: Docker Permission Issues on EC2
**Problem:** Could not run the docker image.
**Solution:** the Docker file creation was not properly created. I created DockerFile instead of 'Dockerfile'.

### Challenge 2: GitHub Actions SSH Connection Failed
**Problem:** SSH deployment step failed with permission denied
**Solution:** Change of permission via Gitbash

### Challenge 3: Application Not Accessible After Deployment
**Problem:** Could not access app via EC2 public IP
**Solution:** Restarted the EC2 instance

## Lessons Learned
- Docker layer caching for faster builds
- Managing secrets securely with GitHub Actions
- Debugging containerized applications using logs
- Infrastructure automation saves time and reduces errors


## Author
**Biodun**
- GitHub: (https://github.com/biodundosco) 
- LinkedIn: (www.linkedin.com/in/abiodundosunmu)
- Email: biodundosunmu@gmail.com

