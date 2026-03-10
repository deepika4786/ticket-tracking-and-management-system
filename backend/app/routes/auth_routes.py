from fastapi import APIRouter
from app.models.user_model import User
from app.database import users_collection

router = APIRouter()

@router.post("/register")
def register(user: User):

    user_dict = user.dict()

    users_collection.insert_one(user_dict)

    return {
        "message": "User registered successfully"
    }