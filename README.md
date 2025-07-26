# Login Proyecto – React + Django

Este es un proyecto de autenticación simple con frontend en **React** y backend en **Django REST Framework**, diseñado para desplegarse en la nube utilizando **AWS Amplify** (frontend) y **AWS Elastic Beanstalk** (backend).

---

## 📁 Estructura del Proyecto

login-proyecto/
├── backend/ # Proyecto Django
├── frontend/ # Proyecto React
├── amplify.yml # Configuración de Amplify para CI/CD (solo frontend)

---

## 🚀 Requisitos

Local:
- Node.js (v16 o superior)
- Python 3.10+
- pip
- virtualenv

Despliegue (opcional):
- Cuenta en [AWS](https://aws.amazon.com/)
- Git y GitHub
- AWS CLI
- Elastic Beanstalk CLI
- Amplify Console configurado

---

## 🧑‍💻 Ejecutar el Proyecto Localmente

1. Clonar repositorio

- git clone https://github.com/Raul-Verdin/login-proyecto.git
- cd login-proyecto


2. Backend – Django

- cd backend
- python -m venv venv
- source venv/bin/activate  # En Windows: venv\Scripts\activate
- pip install -r requirements.txt

# Migrar base de datos
- python manage.py migrate

# Correr el servidor
- python manage.py runserver
- Backend disponible en: http://localhost:8000


3. Frontend – React

- cd ../frontend
- npm install
- npm start
- Frontend en: http://localhost:3000


---


## ☁️ Despliegue en AWS

🔧 Backend (Django) – Elastic Beanstalk
1. Crear entorno en Elastic Beanstalk (Python 3.x)

2. Crear archivo application.py con la instancia WSGI:
- from backend.wsgi import application

3. Instalar EB CLI y hacer login:
- pip install awsebcli
- eb init
- eb create login-backend-env

4. Subir:
- eb deploy

✅ Accede a la URL del backend público (ej. http://login-backend-env.elasticbeanstalk.com/)


---


## 🌐 Frontend (React) – Amplify

1. Ir a AWS Amplify Console

2. Conectar con tu repositorio de GitHub: https://github.com/Raul-Verdin/login-proyecto

3. Asegúrate de que se detecte automáticamente el archivo amplify.yml con esta configuración:
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - cd frontend
        - npm install
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: frontend/build
    files:
      - '**/*'
  cache:
    paths:
      - frontend/node_modules/**/*

4. Guardar y desplegar
✅ La URL pública se generará automáticamente (ej. https://main.d2vuvbx8wng0o4.amplifyapp.com)


---
