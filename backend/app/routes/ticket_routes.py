from fastapi import APIRouter
from pydantic import BaseModel
import joblib
from app.database import tickets_collection

router = APIRouter()

# Request model
class TicketRequest(BaseModel):
    text: str


# Load ML model
model = joblib.load("ml/ticket_model.pkl")
vectorizer = joblib.load("ml/vectorizer.pkl")


# -------- CLASSIFY TICKET --------
@router.post("/classify-ticket")
def classify_ticket(ticket: TicketRequest):

    text = ticket.text

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    return {
        "ticket_text": text,
        "category": prediction
    }


# -------- CREATE TICKET --------
@router.post("/create-ticket")
def create_ticket(ticket: TicketRequest):

    text = ticket.text

    # ML prediction
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    # Team assignment
    team_map = {
        "network": "Network Team",
        "software": "Software Team",
        "hardware": "Hardware Team",
        "access": "Access Team"
    }

    assigned_team = team_map.get(prediction, "Support Team")

    ticket_data = {
        "text": text,
        "category": prediction,
        "assigned_team": assigned_team,
        "status": "open"
    }

    # Save to MongoDB
    tickets_collection.insert_one(ticket_data)

    return {
        "message": "Ticket created successfully",
        "category": prediction,
        "assigned_team": assigned_team
    }