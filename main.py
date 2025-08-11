from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import init_db
from routers import math_router
from auth import authenticate_user, create_access_token

app = FastAPI(
    title="Math Microservice API",
    description="Microserviciu care oferă operații matematice + JWT + Redis + SQLite",
    version="1.0.0"
)

# Inițializare DB
init_db()

# Înregistrare rute
app.include_router(math_router.router, prefix="/api")

# Endpoint login JWT
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=400, detail="Autentificare eșuată")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Health check
@app.get("/")
def root():
    return {"status": "ok"}
