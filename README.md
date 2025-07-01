# 🔗 URL Shortener API
https://roadmap.sh/projects/url-shortening-service

A simple Flask-based RESTful API that shortens long URLs, tracks access stats, and provides redirect support. Includes a minimal HTML frontend.

---

## 📦 Features

- Shorten long URLs with randomly generated short codes
- Redirect using `/r/<shortCode>`
- Track number of times each short URL was accessed
- CRUD operations via REST API
- Minimal frontend using HTML + JS

---

## 🚀 Tech Stack

- Python 3.x
- Flask
- Flask SQLAlchemy
- SQLite (for simplicity)

---

## 📂 Project Structure
```
url-shortener-api/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── utils.py
│ └── templates/
      └── index.html
├── run.py
├── README.md
```

## 📬 API Endpoints
### Create Short URL
```
POST /shorten
{
  "url": "https://long.url"
}
```
### Retrieve Original
```
GET /shorten/<shortCode>
```
### Update
```
PUT /shorten/<shortCode>
{
  "url": "https://new.url"
}
```
### Delete
```
DELETE /shorten/<shortCode>
```
### Stats
```
GET /shorten/<shortCode>/stats
```
### Redirect
```
GET /r/<shortCode>
```

