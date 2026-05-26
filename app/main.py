from fastapi import FastAPI
from app.database import Base, engine
from app.routes.client_routes import router as ClientRoutes

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(ClientRoutes)

@app.get("/")
def index():
    return {"message": "Welcome to the Client API!"}
