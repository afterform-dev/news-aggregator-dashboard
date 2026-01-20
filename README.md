# 📰 News Aggregator Dashboard

Новостной агрегатор Санкт-Петербурга с автоматическим сбором и категоризацией, построенный на FastAPI и React.

## 🧰 Tech Stack

**Backend**
- FastAPI (Python 3.12)
- PostgreSQL 16
- Redis
- Celery + Celery Beat
- OpenAI API

**Frontend**
- React 18
- Axios
- Base CSS

**Infrastructure**
- Docker & Docker Compose
- GitHub Actions (автодеплой)
- Hetzner Cloud (CX22, Ubuntu 24.04)

## 🚀 Quick Start

```bash
cp .env.example .env
# заполните переменные окружения

docker compose up -d --build
```

После запуска:
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- Healthcheck: http://localhost:8000/health

## 📦 Deployment (Hetzner + GitHub Actions)

### 1) Подготовка сервера

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo usermod -aG docker $USER
newgrp docker
```

### 2) Развертывание проекта

```bash
sudo mkdir -p /var/www/news-dashboard
sudo chown -R $USER:$USER /var/www/news-dashboard
cd /var/www/news-dashboard

git clone <your-repo-url> .
cp .env.example .env
nano .env

docker compose up -d --build
```

### 3) Настройка GitHub Actions

Создайте secrets в репозитории:
- `SERVER_HOST`
- `SERVER_USER`
- `SSH_PRIVATE_KEY`

Push в `main` автоматически запустит деплой.

## 🧾 API Documentation

Swagger UI доступен по адресу: http://localhost:8000/docs

## 🖼️ Screenshots

> Добавьте скриншоты интерфейса после первого деплоя.

## 🧭 Команды для GitHub

### Создание репозитория и первый push

```bash
git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/news-aggregator-dashboard.git
git push -u origin main
```

### Добавление GitHub Secrets

```bash
# через GitHub UI
# Settings -> Secrets and variables -> Actions -> New repository secret
```

### Ручной деплой на сервер

```bash
cd /var/www/news-dashboard
git pull origin main
docker compose down
docker compose up -d --build
docker compose ps
```
