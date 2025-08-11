from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Configurație JWT
SECRET_KEY = "secretul_meu_super_tare"  # schimbă în producție!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Obiect de securitate pentru extragerea tokenului
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Context pentru hashing parole
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Utilizator fictiv (pentru test/demo)
fake_user = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123")  # Se regenerează la fiecare run!
}

# Verifică parola
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Verifică dacă userul este valid
def authenticate_user(username: str, password: str) -> bool:
    if username != fake_user["username"]:
        return False
    if not verify_password(password, fake_user["hashed_password"]):
        return False
    return True

# Creează un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Obține userul curent din token
def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid sau lipsă",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
