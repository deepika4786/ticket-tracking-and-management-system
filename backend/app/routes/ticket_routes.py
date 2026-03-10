from app.database import tickets_collection

@router.post("/create-ticket")
def create_ticket(ticket: TicketRequest):

    text = ticket.text

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

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

    tickets_collection.insert_one(ticket_data)

    return {
        "message": "Ticket created successfully",
        "category": prediction,
        "assigned_team": assigned_team
    }