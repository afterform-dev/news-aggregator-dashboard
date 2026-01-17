from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="News Aggregator API",
    description="St. Petersburg News Aggregator with AI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "News Aggregator API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/news")
async def get_news():
    """Get all news articles"""
    return {
        "articles": [
            {
                "id": 1,
                "title": "Тестовая новость 1",
                "content": "Содержание новости...",
                "category": "политика",
                "source": "test",
                "published_at": "2026-01-17T10:00:00"
            }
        ],
        "total": 1
    }

@app.get("/api/categories")
async def get_categories():
    """Get all categories"""
    return {
        "categories": [
            "политика",
            "экономика",
            "общество",
            "культура",
            "спорт",
            "технологии"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
