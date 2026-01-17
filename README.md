# 📰 News Aggregator Dashboard

Агрегатор новостей Санкт-Петербурга с AI-powered анализом и категоризацией.

## 🚀 Features

- 📡 Автоматический сбор новостей из RSS/Telegram
- 🤖 AI-обработка через OpenAI GPT-4
- 🏷️ Автоматическая категоризация
- 📊 Dashboard с фильтрацией
- 🔄 Real-time обновления
- 📱 Telegram бот для уведомлений

## 🛠️ Tech Stack

**Backend:**
- FastAPI (Python)
- PostgreSQL
- Redis
- Celery (background tasks)
- OpenAI API

**Frontend:**
- React
- TailwindCSS
- Axios

**Infrastructure:**
- Docker & Docker Compose
- Nginx (production)
- Hetzner Cloud

## 📦 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/news-aggregator-dashboard.git
cd news-aggregator-dashboard
```

### 2. Configure Environment

```bash
cp .env.example .env
nano .env
```

Заполни:
- `POSTGRES_PASSWORD` - придумай надёжный пароль
- `SECRET_KEY` - сгенерируй: `openssl rand -hex 32`
- `OPENAI_API_KEY` - твой API ключ OpenAI
- `TELEGRAM_BOT_TOKEN` - токен бота (опционально)

### 3. Start Services

```bash
docker compose up -d
```

### 4. Initialize Database

```bash
docker compose exec api python -c "from backend.database import init_db; init_db()"
```

### 5. Access

- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- API: http://localhost:8000/api

## 📁 Project Structure

```
news-aggregator-dashboard/
├── backend/
│   ├── api/              # FastAPI routes
│   ├── models/           # Database models
│   ├── services/         # Business logic
│   ├── tasks/            # Celery tasks
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Pages
│   │   └── api/          # API client
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🔧 Development

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## 🚀 Deployment

### Production на Hetzner

1. **Создай сервер:**
   - CX22 (4GB RAM, 2 vCPU)
   - Ubuntu 24.04
   - Nuremberg location

2. **Настрой сервер:**
```bash
# Используй setup скрипт
bash setup-server.sh
```

3. **Deploy:**
```bash
cd /var/www/news-dashboard
git clone <repo-url> .
cp .env.example .env
nano .env  # настрой переменные
docker compose up -d
```

### CI/CD через GitHub Actions

Push в `main` → автоматический деплой на сервер!

## 📊 Monitoring

```bash
# Статус контейнеров
docker compose ps

# Логи
docker compose logs -f api
docker compose logs -f celery

# Ресурсы
docker stats
```

## 🔐 Security

- ✅ SSH только по ключу
- ✅ Firewall (UFW)
- ✅ Secrets в .env (не в git)
- ✅ HTTPS (через Certbot)
- ✅ Rate limiting на API

## 📝 API Documentation

После запуска: http://localhost:8000/docs

Основные endpoints:
- `GET /api/news` - список новостей
- `GET /api/news/{id}` - одна новость
- `GET /api/categories` - категории
- `POST /api/news/refresh` - обновить новости

## 🤝 Contributing

1. Fork проект
2. Создай feature branch (`git checkout -b feature/amazing`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing`)
5. Открой Pull Request

## 📄 License

MIT

## 👤 Author

Anthony Ginsbrook

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- Hetzner for hosting
- FastAPI & React communities
