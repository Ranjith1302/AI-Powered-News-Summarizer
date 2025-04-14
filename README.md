
# 📰 AI News Generator 🧠🌐

An intelligent, auto-updating news aggregator built with **Django**, **Google Gemini AI**, **NewsAPI**, and **Unsplash API**. This app fetches trending news, summarizes it using **Gemini Pro**, adds relevant images, and displays everything on a clean Django-based frontend. Fully deployed and ready to go!

## 🚀 Features

- ✨ Auto-fetch trending news from trusted sources (BBC, CNN, Reuters, etc.)
- 🧠 Summarizes news using **Google Gemini AI**
- 🖼️ Fetches dynamic, relevant images using **Unsplash**
- 🕒 Background scheduling with **APScheduler**
- 🌐 Django frontend with live deployment

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/587d1f5b-f16a-4cd8-8c88-2e8d80fc6a99)

---

## 🧩 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Django templates + Bootstrap/CSS
- **AI**: Google Gemini Pro
- **News Data**: NewsAPI.org
- **Images**: Unsplash API
- **Scheduler**: APScheduler (background task runner)
- **Deployment**: (e.g. Vercel, Render, Railway, Heroku — specify yours)

---

## 🔑 API Keys (Required)

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_google_gemini_api_key
NEWS_API_KEY=your_newsapi_key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
```

---

## 📦 Requirements

Install via `pip` or `requirements.txt`

```bash
pip install -r requirements.txt
```

### `requirements.txt` Example

```
Django>=4.2
requests
python-dotenv
google-generativeai
beautifulsoup4
apscheduler
gunicorn  # if deploying
whitenoise  # for static files in production
```

---

## 🛠️ Project Setup

```bash
# Clone the repo
git clone https://github.com/your-username/ai-news-django.git
cd ai-news-django

# Install dependencies
pip install -r requirements.txt

# Add your API keys to .env
touch .env  # then add the keys

# Run migrations
python manage.py migrate

# Start the dev server
python manage.py runserver
```

---

## ⚙️ Scheduler Setup

Make sure `fetch_trending_news()` runs periodically.

In your `apps.py` or `ready()` method in any app:

```python
from apscheduler.schedulers.background import BackgroundScheduler
from .news_updater import fetch_trending_news

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_trending_news, "interval", hours=1)
scheduler.start()
```

> 🛑 Be sure to handle `scheduler.shutdown()` when stopping Django gracefully.

---


## ☁️ Deployment

You can deploy this project using:
- **Vercel** (with Python backend integration)
- **Render**
- **Railway**
- **Heroku**
- **Docker + VPS**

Make sure:
- Your `.env` variables are set in the platform
- Static files are handled with `WhiteNoise` or appropriate configuration
- You use `gunicorn` or `uvicorn` as production server

---



---



