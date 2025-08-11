from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas
import redis
from logger_config import logger
from operations import operations
from auth import get_current_user
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

router = APIRouter()

@router.post("/pow", response_model=schemas.OperationResponse)
def compute_pow(req: schemas.OperationRequest, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    try:
        logger.info(f"[{user}] Calculăm pow pentru {req.number}")
        result = str(req.number ** 2)
        crud.log_request(db, "pow", str(req.number), result)
        return schemas.OperationResponse(operation="pow", input_value=str(req.number), result=result)
    except Exception as e:
        logger.exception("Eroare la /pow")
        raise HTTPException(status_code=500, detail="Eroare internă la /pow")

@router.post("/factorial", response_model=schemas.OperationResponse)
def compute_factorial(
    req: schemas.OperationRequest,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    try:
        logger.info(f"[{user}] Calculăm factorial pentru {req.number}")

        def fact(n):
            if n < 0:
                raise ValueError("Factorialul nu este definit pentru numere negative.")
            return 1 if n <= 1 else n * fact(n - 1)

        result = str(fact(req.number))
        crud.log_request(db, "factorial", str(req.number), result)
        return schemas.OperationResponse(
            operation="factorial",
            input_value=str(req.number),
            result=result
        )

    except ValueError as ve:
        logger.warning(f"Eroare validare la /factorial: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        logger.exception("Eroare internă la /factorial")
        raise HTTPException(status_code=500, detail="Eroare internă la /factorial")


@router.post("/fibonacci", response_model=schemas.OperationResponse)
def compute_fibonacci(req: schemas.OperationRequest, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    try:
        logger.info(f"[{user}] Calculăm Fibonacci pentru n={req.number}")

        def fib(n):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a

        cached = r.get(f"fibonacci:{req.number}")
        if cached:
            logger.info(f"Fibonacci({req.number}) găsit în cache: {cached}")
            return schemas.OperationResponse(operation="fibonacci", input_value=str(req.number), result=cached)

        result = str(fib(req.number))
        r.setex(f"fibonacci:{req.number}", 3600, result)

        crud.log_request(db, "fibonacci", str(req.number), result)
        return schemas.OperationResponse(operation="fibonacci", input_value=str(req.number), result=result)

    except Exception as e:
        logger.exception("Eroare la /fibonacci")
        raise HTTPException(status_code=500, detail="Eroare internă la /fibonacci")



@router.post("/op/{operation_name}", response_model=schemas.OperationResponse)
def compute_generic(
    operation_name: str,
    req: schemas.OperationRequest,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    logger.info(f"[{user}] Executăm operația generică: {operation_name} pentru {req.number}")

    if operation_name not in operations:
        logger.warning(f"Operația '{operation_name}' nu este disponibilă.")
        raise HTTPException(status_code=404, detail="Operația nu este disponibilă.")

    func = operations[operation_name]
    result = str(func(req.number))

    crud.log_request(db, operation_name, str(req.number), result)
    return schemas.OperationResponse(operation=operation_name, input_value=str(req.number), result=result)
