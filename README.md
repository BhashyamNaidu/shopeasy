# ShopEasy

A cloud-native e-commerce backend application built using FastAPI, MySQL, Docker, and AWS. The project demonstrates modern backend development, cloud deployment, containerization, monitoring, and CI/CD automation.

---

## Project Highlights

- Developed a RESTful backend using FastAPI and SQLAlchemy.
- Deployed on AWS EC2 with Docker and Nginx.
- Integrated Amazon RDS MySQL for persistent data storage.
- Configured an Application Load Balancer (ALB) with health checks.
- Implemented monitoring and alerting using CloudWatch and SNS.
- Automated deployments using GitHub Actions CI/CD pipelines.
- Built and managed AWS infrastructure including VPC, Security Groups, EC2, RDS, ALB, CloudWatch, and SNS.

---

## Features

- Product CRUD API
- FastAPI REST endpoints
- SQLAlchemy ORM integration
- Amazon RDS MySQL database
- Dockerized deployment
- Nginx reverse proxy
- Application Load Balancer (ALB)
- CloudWatch monitoring
- SNS email alerts
- GitHub Actions CI/CD pipeline

---

## Architecture

```text
                        ┌──────────────┐
                        │    Users     │
                        └──────┬───────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Application Load Balancer│
                  └───────────┬─────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │      Nginx      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   SQLAlchemy    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Amazon RDS MySQL│
                    └─────────────────┘


     GitHub ──► GitHub Actions ──► EC2 Deployment

     CloudWatch ──► SNS Email Alerts
```

---

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- Amazon RDS (MySQL)

### Infrastructure

- Amazon EC2
- Application Load Balancer (ALB)
- Amazon VPC
- Security Groups

### DevOps

- Docker
- Docker Compose
- Nginx
- GitHub Actions
- CloudWatch
- SNS

---

## API Endpoints

### Health Check

```http
GET /health
```

### Products

```http
GET /products
```

```http
POST /products
```

```http
PUT /products/{product_id}
```

```http
DELETE /products/{product_id}
```

---

## CI/CD Pipeline

```text
Developer Pushes Code
            │
            ▼
      GitHub Repository
            │
            ▼
      GitHub Actions
            │
            ▼
     SSH into AWS EC2
            │
            ▼
 Docker Compose Deployment
            │
            ▼
 Updated Production Application
```

---

## Monitoring & Alerts

- CloudWatch CPU utilization alarms
- SNS email notifications
- ALB health checks
- Application health endpoint monitoring

---

## Deployment

The application is deployed on AWS using:

- EC2 for application hosting
- Docker containers for packaging
- Nginx reverse proxy
- Amazon RDS MySQL database
- Application Load Balancer for traffic routing
- GitHub Actions for automated deployments

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Cloud-native application deployment
- AWS networking and infrastructure
- Containerization with Docker
- CI/CD automation
- Monitoring and alerting
- Load balancing and health checks
- Production-style backend architecture

---

## Author

**Bhashyam Naidu**

GitHub: https://github.com/BhashyamNaidu

Repository: https://github.com/BhashyamNaidu/shopeasy
