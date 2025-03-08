# Car Dealership - Full Stack Capstone Project

## Project Overview
This project is a Full Stack web application developed as part of the IBM Full Stack Software Developer Professional Certificate on Coursera. The application is designed for a national car dealership, allowing users to browse dealerships, view and submit reviews, and manage car make and model data. It incorporates both front-end and back-end technologies, following cloud-native and containerized deployment practices.

## Features
- **User Authentication**: User registration, login, and logout using Django authentication.
- **Dealership Information**: View dealership details, filter by state, and check customer reviews.
- **Review System**: Submit and analyze customer reviews using an IBM Cloud-hosted sentiment analysis service.
- **Admin Management**: Manage car make, model, and dealership data via the Django admin panel.
- **CI/CD Pipeline**: Automated deployment using GitHub Actions, Docker, and Kubernetes.
- **Cloud Deployment**: Hosted using IBM Cloud Code Engine and Kubernetes for scalability.

## Tech Stack
### Frontend:
- React.js
- Bootstrap
- HTML/CSS

### Backend:
- Django (Python)
- Express.js (Node.js)
- MongoDB (for dealer and review data storage)
- SQLite (for car make/model data storage)

### Cloud & DevOps:
- IBM Cloud Code Engine (Sentiment Analysis Service Deployment)
- Kubernetes (Containerized Deployment)
- Docker (Containerization)
- GitHub Actions (CI/CD Automation)

## System Architecture
- **Django Backend**: Manages user authentication, proxy services, and the admin panel.
- **React Frontend**: Provides an intuitive user interface for customers and administrators.
- **Express.js & MongoDB**: Handles dealership and review data, ensuring seamless API interactions.
- **Sentiment Analysis Service**: Hosted on IBM Cloud Code Engine to analyze review sentiments.
- **CI/CD Pipeline**: Automates testing, linting, and deployment to a Kubernetes cluster.


## Repository & References
- **GitHub Repo**: [Project Repository](https://github.com/aysait101/xrwvm-fullstack_developer_capstone)
- **Django Documentation**: [Django Docs](https://docs.djangoproject.com/en/stable/)
- **MongoDB Documentation**: [MongoDB Docs](https://docs.mongodb.com/manual/)
- **React Documentation**: [React Docs](https://reactjs.org/docs/getting-started.html)


