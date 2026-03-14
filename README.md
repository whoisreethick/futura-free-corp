# Futura 💌

An anonymous message app where strangers leave notes for your name.

Type your name. See what the world has to say.

---

## What is this?

Futura is a full stack web app built as a learning project.
You enter your name and instantly see anonymous messages left by strangers
for anyone who shares your name — from around the world.
Leave one too.

---

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python + FastAPI |
| Database | SQLite (PostgreSQL on production) |
| Frontend | HTML + CSS + Vanilla JS |
| Fonts | Fjalla One + Courier Prime |
| Container | Docker |
| CI/CD | GitHub Actions |
| Hosting | Render (coming soon) |

---

## Project Structure
```
futura-free-corp/
├── main.py          # FastAPI routes
├── database.py      # Database connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── index.html       # Frontend
├── Dockerfile       # Container config
├── requirements.txt # Dependencies
└── .github/
    └── workflows/
        └── deploy.yml  # CI/CD pipeline
```

---

## Running Locally

### Without Docker
```bash
# Clone the repo
git clone https://github.com/whoisreethick/futura-free-corp.git
cd futura-free-corp

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

Open `index.html` in your browser.

### With Docker
```bash
docker build -t futura .
docker run -p 8000:8000 -v futura_data:/app futura
```

Open `index.html` in your browser.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/messages/{name}` | Get all messages for a name |
| POST | `/messages/` | Leave an anonymous message |

---

## What I learned building this

- REST API design with FastAPI
- Database modeling with SQLAlchemy
- Data validation with Pydantic
- Containerization with Docker
- CI/CD pipelines with GitHub Actions
- Frontend ↔ Backend communication with fetch()
- Persistent storage with Docker Volumes

---

## Roadmap

- [ ] Deploy live on Render
- [ ] Swap SQLite for PostgreSQL
- [ ] Add message reactions
- [ ] Rate limiting to prevent spam
- [ ] Search by name with autocomplete

---

Built in public by [@whoisreethick](https://github.com/whoisreethick) 🚀
