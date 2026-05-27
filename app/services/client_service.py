from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client_schema import ClientCreate

def create_client(db: Session, client: ClientCreate):
    try: 
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
    except Exception as e:
        db.rollback()
        raise e

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client: Client):
    client_db = db.query(Client).filter(Client.id == client_id).first()
    if not client_db:
        raise ValueError("Client not found")
    try:
        client_db.name = client.name
        client_db.email = client.email
        client_db.phone = client.phone
        client_db.document = client.document
        db.commit()
        db.refresh(client_db)
        return client_db
    except Exception as e:
        db.rollback()
        raise e

def delete_client(db: Session, client_id: int):
    client_db = db.query(Client).filter(Client.id == client_id).first()
    if not client_db:
        raise ValueError("Client not found")
    try:
        db.delete(client_db)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
