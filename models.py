from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class RequestLog(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String(50), index=True)
    input_value = Column(String(100))
    result = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
