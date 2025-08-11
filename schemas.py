from pydantic import BaseModel, Field

class OperationRequest(BaseModel):
    number: int = Field(..., example=5)

class OperationResponse(BaseModel):
    operation: str = Field(..., example="fibonacci")
    input_value: str = Field(..., example="5")
    result: str = Field(..., example="5")
