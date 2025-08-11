from models import RequestLog
from sqlalchemy.orm import Session

def log_request(db: Session, operation: str, input_value: str, result: str) -> RequestLog:
    log = RequestLog(operation=operation, input_value=input_value, result=result)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
