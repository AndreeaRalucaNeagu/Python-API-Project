from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./requests.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Funcție pentru creare DB (opțional)
def init_db():
    from models import Base  # se importă doar la execuție
    Base.metadata.create_all(bind=engine)

# Generator pentru injectare DB (evită duplicarea în fiecare router)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
