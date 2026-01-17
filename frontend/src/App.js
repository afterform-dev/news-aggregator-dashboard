import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/news')
      .then(res => res.json())
      .then(data => {
        setNews(data.articles || []);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>📰 Новости Санкт-Петербурга</h1>
      </header>
      
      <main className="container">
        {loading ? (
          <p>Загрузка...</p>
        ) : (
          <div className="news-grid">
            {news.map(article => (
              <div key={article.id} className="news-card">
                <span className="category">{article.category}</span>
                <h2>{article.title}</h2>
                <p>{article.content}</p>
                <small>{new Date(article.published_at).toLocaleString('ru-RU')}</small>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
