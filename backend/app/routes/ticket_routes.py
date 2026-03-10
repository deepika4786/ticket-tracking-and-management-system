from fastapi import APIRouter
from pydantic import BaseModel
import joblib

router = APIRouter()

# request body schema
class TicketRequest(BaseModel):
    text: str

model = joblib.load("ml/ticket_model.pkl")
vectorizer = joblib.load("ml/vectorizer.pkl")


@router.post("/classify-ticket")
def classify_ticket(ticket: TicketRequest):

    text = ticket.text

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    return {
        "ticket_text": text,
        "category": prediction
    }