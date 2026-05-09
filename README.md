# MLOps Data Science Network Security with AWS

An end-to-end MLOps and Data Science project focused on automated phishing detection and secure cloud deployment using AWS, Docker, CI/CD pipelines, and machine learning workflows.

---

## Project Overview

This project demonstrates how to build, containerize, automate, and deploy a machine learning-based network security application using modern MLOps practices.

The system includes:

- Machine Learning model training for phishing detection
- Dockerized application deployment
- CI/CD automation using GitHub Actions
- AWS cloud deployment workflows
- End-to-end automation from development to production
- Scalable backend infrastructure for ML applications

The goal of this project is to simulate a production-ready machine learning deployment pipeline similar to real-world enterprise environments.

---

## Features

- End-to-end MLOps workflow
- Automated CI/CD pipeline
- Docker containerization
- AWS cloud deployment
- GitHub Actions automation
- Machine Learning phishing detection model
- Reproducible ML pipeline
- Backend deployment automation
- Modular project structure
- Production-oriented architecture

---

## Tech Stack

### Programming & ML
- Python
- Scikit-learn
- Pandas
- NumPy

### MLOps & DevOps
- Docker
- GitHub Actions
- CI/CD Pipelines

### Cloud
- AWS EC2
- AWS ECR
- AWS S3

### Backend & Deployment
- Flask / FastAPI
- REST APIs

---

## Project Architecture

```text
Developer Push
       ↓
GitHub Repository
       ↓
GitHub Actions CI/CD
       ↓
Docker Image Build
       ↓
AWS ECR Push
       ↓
AWS EC2 Deployment
       ↓
Production ML Service
```

---

# Folder Structure

```bash
├── .github/workflows/
│   └── ci-cd.yaml
├── artifacts/
├── notebooks/
├── src/
├── templates/
├── static/
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

## CI/CD Workflow

The project uses GitHub Actions to automate the deployment lifecycle.

Pipeline stages include:

1. Code push to GitHub
2. Automated build process
3. Docker image creation
4. AWS ECR authentication
5. Docker image push to ECR
6. EC2 deployment automation
7. Production deployment update

---

## Machine Learning Workflow

The ML pipeline includes:

- Data ingestion
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Model persistence
- Inference pipeline

The phishing detection model is designed to classify potentially malicious network or phishing-related inputs using supervised learning techniques.

---

## Docker Deployment

The application is fully containerized using Docker to ensure:

- Environment consistency
- Easy deployment
- Scalability
- Reproducibility
- Cloud portability

Run locally:

```bash
docker build -t network-security-app .
docker run -p 5000:5000 network-security-app
```

---

## AWS Deployment

The deployment workflow uses AWS services including:

- EC2 for hosting
- ECR for Docker image registry
- S3 for artifact storage

Deployment process:

1. Build Docker image
2. Push image to AWS ECR
3. Pull image on EC2 instance
4. Run containerized ML service

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/Oday-Najad/MLOps-Data-Science-Network-Security-with-AWS.git
cd MLOps-Data-Science-Network-Security-with-AWS
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Key Learning Outcomes

This project demonstrates practical experience with:

- Machine Learning Engineering
- MLOps workflows
- CI/CD automation
- Cloud deployment
- Docker containerization
- AWS infrastructure
- Production-oriented ML systems
- Backend engineering
- Automation pipelines

---

## Future Improvements

- Kubernetes deployment
- Monitoring and logging
- Model versioning
- MLflow integration
- Automated retraining pipelines
- Infrastructure as Code (Terraform)
- Advanced cloud scaling

---

## Author

### Oday Najad

Back-end / AI Engineer

- GitHub: https://github.com/Oday-Najad
- LinkedIn: https://www.linkedin.com/in/oday-najad/

---

## Repository

https://github.com/Oday-Najad/MLOps-Data-Science-Network-Security-with-AWS
