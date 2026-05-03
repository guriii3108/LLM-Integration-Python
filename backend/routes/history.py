# Import APIRouter and HTTPException for error handling
from fastapi import APIRouter, HTTPException
# Import our database query functions
from db.crud import get_all_chats, get_chat_with_qa

# Initialize the router for history-related endpoints
router = APIRouter()

# Define a GET endpoint at "/history" to fetch the list of all chats
@router.get("/history")
def get_history_list():
    # Call the database function to get all chats
    chats = get_all_chats()
    # Return the list of chats to the frontend
    return chats

# Define a GET endpoint with a dynamic path parameter "{chat_id}"
@router.get("/history/{chat_id}")
# The chat_id variable is automatically extracted from the URL
def get_chat_detail(chat_id: str):
    # Call the database function to get the specific chat and all its messages
    chat = get_chat_with_qa(chat_id)
    
    # If the database returns None (meaning the chat wasn't found), throw a 404 Error
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
        
    # Otherwise, return the chat details to the frontend
    return chat

