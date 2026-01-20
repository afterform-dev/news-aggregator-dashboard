import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/news');
        setNews(response.data.articles || []);
      } catch (err) {
        console.error(err);
        setError('Не удалось загрузить новости. Попробуйте позже.');
      } finally {
        setLoading(false);
      }
    };

    fetchNews();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>📰 Новости Санкт-Петербурга</h1>
      </header>

      <main className="container">
        {loading && <p className="status">Загрузка...</p>}
        {error && <p className="status error">{error}</p>}
        {!loading && !error && (
          <div className="news-grid">
            {news.map((article) => (
              <article key={article.id} className="news-card">
                <span className="category">{article.category}</span>
                <h2>{article.title}</h2>
                <p>{article.content}</p>
                <div className="card-footer">
                  <small>{new Date(article.published_at).toLocaleString('ru-RU')}</small>
                </div>
              </article>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
