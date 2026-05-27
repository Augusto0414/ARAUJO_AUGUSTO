from fastapi import APIRouter,Depends
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.schemas.client_schema import ClientCreate
from app.models.client import Client

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@router.post("/")
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    newClient = Client(
        name=client.name,
        email=client.email,
        phone=client.phone,
        document=client.document
    )
    db.add(newClient)
    db.commit()
    db.refresh(newClient)
    return newClient

@router.get("/")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.get("/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(Client).filter(Client.id == client_id).first()