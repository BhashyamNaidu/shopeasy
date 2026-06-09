# ShopEasy

Cloud-native e-commerce backend application built using FastAPI, MySQL, Docker, and AWS.

## Features

* Product CRUD API
* FastAPI REST endpoints
* SQLAlchemy ORM integration
* Amazon RDS MySQL database
* Dockerized deployment
* Nginx reverse proxy
* Application Load Balancer (ALB)
* CloudWatch monitoring
* SNS email alerts
* GitHub Actions CI/CD pipeline

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Python

### Database

* Amazon RDS (MySQL)

### Infrastructure

* Amazon EC2
* Application Load Balancer
* Security Groups
* VPC

### DevOps

* Docker
* Docker Compose
* GitHub Actions
* CloudWatch
* SNS

## API Endpoints

### Health Check

GET /health

### Products

GET /products

POST /products

PUT /products/{id}

DELETE /products/{id}

## Architecture

Client
→ Application Load Balancer
→ Nginx
→ FastAPI
→ SQLAlchemy
→ Amazon RDS MySQL

## CI/CD Pipeline

Git Push
→ GitHub Actions
→ SSH to EC2
→ Docker Compose Deployment

## Author

Bhashyam Naidu
