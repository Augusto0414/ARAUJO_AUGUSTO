from fastapi import APIRouter,Depends,HTTPException
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.schemas.client_schema import ClientCreate
from app.services.client_service import (create_client, get_client, get_client_by_id, update_client, delete_client)

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@router.post("/")
def create(client: ClientCreate, db: Session = Depends(get_db)):
    try:
        return create_client(db, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def get_clients(db: Session = Depends(get_db)):
    try:
        return get_client(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    try:
        return get_client_by_id(db, client_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{client_id}")
def update(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    try:
        return update_client(db, client_id, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/{client_id}")
def delete(client_id: int, db: Session = Depends(get_db)):
    try:
        return delete_client(db, client_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
