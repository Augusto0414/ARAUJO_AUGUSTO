from pydantic import BaseModel

class PolicyCreate(BaseModel):
    client_id: int
    policy_number: str
    coverage_amount: int
    start_date: str
    end_date: str

class Policy(PolicyCreate):
    id: int
    
    class Config:
        orm_mode = True    
