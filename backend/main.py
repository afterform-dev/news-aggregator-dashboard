from datetime import datetime
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import or_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import Article, get_db

app = FastAPI(
    title="News Aggregator API",
    description="St. Petersburg News Aggregator with AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MOCK_ARTICLES = [
    {
        "id": 1,
        "title": "Открытие нового парка в центре города",
        "content": "В Санкт-Петербурге открыли новый парк с зонами отдыха и велодорожками.",
        "category": "общество",
        "source": "mock",
        "url": "https://example.com/news/park",
        "published_at": "2026-01-17T10:00:00",
        "created_at": "2026-01-17T10:00:00",
    },
    {
        "id": 2,
        "title": "Транспортная развязка снизит пробки",
        "content": "Новая развязка на юге города ускорит движение и сократит время в пути.",
        "category": "город",
        "source": "mock",
        "url": "https://example.com/news/traffic",
        "published_at": "2026-01-16T09:30:00",
        "created_at": "2026-01-16T09:30:00",
    },
    {
        "id": 3,
        "title": "Фестиваль науки соберет студентов",
        "content": "В Невском районе пройдет фестиваль науки и технологий для школьников.",
        "category": "технологии",
        "source": "mock",
        "url": "https://example.com/news/science",
        "published_at": "2026-01-15T08:00:00",
        "created_at": "2026-01-15T08:00:00",
    },
]


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/api/news")
async def get_news(
    category: Optional[str] = Query(default=None),
    source: Optional[str] = Query(default=None),
    search: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    try:
        statement = select(Article)
        if category:
            statement = statement.where(Article.category == category)
        if source:
            statement = statement.where(Article.source == source)
        if search:
            statement = statement.where(
                or_(
                    Article.title.ilike(f"%{search}%"),
                    Article.content.ilike(f"%{search}%"),
                )
            )
        articles = db.execute(statement).scalars().all()
    except SQLAlchemyError:
        articles = []

    if not articles:
        return {"articles": MOCK_ARTICLES, "total": len(MOCK_ARTICLES)}

    response = [
        {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "category": article.category,
            "source": article.source,
            "url": article.url,
            "published_at": article.published_at.isoformat(),
            "created_at": article.created_at.isoformat(),
        }
        for article in articles
    ]
    return {"articles": response, "total": len(response)}


@app.get("/api/news/{article_id}")
async def get_news_item(article_id: int, db: Session = Depends(get_db)):
    try:
        article = db.execute(select(Article).where(Article.id == article_id)).scalar_one_or_none()
    except SQLAlchemyError:
        article = None

    if article:
        return {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "category": article.category,
            "source": article.source,
            "url": article.url,
            "published_at": article.published_at.isoformat(),
            "created_at": article.created_at.isoformat(),
        }

    for mock in MOCK_ARTICLES:
        if mock["id"] == article_id:
            return mock

    raise HTTPException(status_code=404, detail="Article not found")


@app.get("/api/categories")
async def get_categories(db: Session = Depends(get_db)):
    categories: List[str] = []
    try:
        results = db.execute(select(Article.category).distinct()).all()
        categories = [row[0] for row in results if row[0]]
    except SQLAlchemyError:
        categories = []

    if not categories:
        categories = ["политика", "экономика", "общество", "культура", "спорт", "технологии"]

    return {"categories": categories}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
