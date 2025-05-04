# SimpleAPI

SimpleAPI is a minimal RESTful API built using FastAPI and SQLAlchemy. It supports project creation with automatic ID management, duplicate prevention, and Nginx reverse proxy support for production deployments.

---

## ✨ Features

- ✅ FastAPI backend with SQLite database
- ✅ SQLAlchemy ORM for project persistence
- ✅ Automatic, gapless project ID assignment (fills deleted ID slots)
- ✅ Duplicate project prevention
- ✅ Production-ready configuration with Nginx
- ✅ Easily extensible for additional models and routes

---

## 📁 Project Structure

```
simpleapi/
├── app/
│   ├── main.py              # FastAPI app
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   └── database.py          # DB session and engine setup
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Darkboy17/simpleapi.git
cd simpleapi
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

---

## 🔧 API Endpoints

### Create a new project
**POST** `/projects/`

```json
{
  "name": "MyProject"
}
```

- Assigns the next available ID (reuses deleted IDs).
- Prevents duplicate project names.

### Get all projects
**GET** `/projects/`

---

## 🧠 Behind the Scenes

- **Duplicate prevention** is enforced before inserting a new project.
- **Gapless ID assignment** uses a helper function to fill deleted IDs instead of auto-increment.

---

## 🌐 Nginx Deployment

1. Create a configuration file:
   ```bash
   sudo nano /etc/nginx/sites-available/simpleapi
   ```

2. Sample config:
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. Enable the site and restart Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/simpleapi /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

---

## 📦 Requirements

```
fastapi
uvicorn
sqlalchemy
```

You can generate this with:
```bash
pip freeze > requirements.txt
```

---

## 📄 License

MIT License — free to use and modify.
