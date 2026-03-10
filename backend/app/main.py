from fastapi import FastAPI
from app.routes import ticket_routes

app = FastAPI()

app.include_router(ticket_routes.router)

@app.get("/")
def home():
    return {"message": "Ticket Tracking API Running"}