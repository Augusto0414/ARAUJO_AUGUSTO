from pydantic import BaseModel, EmailStr


class ClientCreate(BaseModel):

    name: str

    phone: str

    email: EmailStr

    document: str


class ClientResponse(ClientCreate):

    id: int

    class Config:
        from_attributes = True