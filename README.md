# 🧮 Math Microservice – FastAPI, JWT, Redis, Docker, SQLite

Acest proiect este un microserviciu REST care oferă operații matematice (putere, factorial, Fibonacci), cu funcționalități moderne precum autentificare JWT, caching cu Redis, persistare în SQLite și containerizare cu Docker.

---

## 🚀 Funcționalități

- ✅ API REST pentru:
  - `pow(x)` – pătratul unui număr
  - `factorial(n)` – calcul recursiv
  - `fibonacci(n)` – valoarea n din șirul lui Fibonacci
- ✅ Endpoint generic extensibil: `/api/op/{operation_name}`
- ✅ Persistarea fiecărei cereri în baza de date SQLite
- ✅ Caching cu Redis pentru rezultate Fibonacci
- ✅ Autentificare cu JWT (`/token`)
- ✅ Protecție endpointuri cu Bearer Token
- ✅ Logare în consolă cu timestamp
- ✅ Docker + Docker Compose pentru rulare completă

---

## 🗂️ Structura proiectului

```
.
├── main.py
├── auth.py
├── database.py
├── models.py
├── crud.py
├── schemas.py
├── operations.py
├── logger_config.py
├── routers/
│   └── math_router.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── requests.db (generat automat)
```

---

## 🐳 Rulare cu Docker

1. Instalează Docker + Docker Compose
2. Clonează acest proiect și din terminal:

```bash
docker compose up --build
```

3. Deschide browserul:

```
http://localhost:8000/docs
```

---

## 🔐 Autentificare

- Endpoint login: `POST /token`
- Credențiale:
  - `username`: `admin`
  - `password`: `admin123`
- După ce primești token-ul, click pe **Authorize** și introdu:
```
Bearer <token>
```

---

## 📦 Exemple de apeluri

### Fibonacci:
```http
POST /api/op/fibonacci
{
  "number": 8
}
```

### Pow:
```http
POST /api/op/pow
{
  "number": 3
}
```

---

## 📝 Tehnologii folosite

- **FastAPI** – framework web rapid și modern
- **Uvicorn** – ASGI server performant
- **SQLite + SQLAlchemy** – ORM și persistare locală
- **Redis** – caching eficient
- **Docker** – rulare izolată și replicabilă
- **JWT** – autentificare securizată
- **Pydantic** – validare request/response

---

## 🔧 ToDo / Extensii posibile

- [ ] Logare în fișier (nu doar consolă)
- [ ] Admin dashboard pentru vizualizarea logurilor
- [ ] Implementare WebSockets pentru operații live
- [ ] Teste unitare cu PyTest

---

## 🧑‍💻 Autor

Proiect realizat de: Neagu Andreea-Raluca 
Pentru evaluare tehnică / interviu / proiect universitar