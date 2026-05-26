from fastapi import APIRouter

from app.schemas.client_schema import ClientCreate

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@router.post("/")
def create_client(client: ClientCreate):

    return {
        "message": "Client created",
        "data": client
    }


@router.get("/")
def get_clients():

    return [
        {
            "id": 1,
            "name": "Juan Perez",
            "phone": "3001234567",
            "email": "juan@gmail.com",
            "document": "123456789"
        }
    ]