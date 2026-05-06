# Import the function that talks to Groq
from services.llm_service import get_llm_response
# Import the database functions
from db.crud import create_chat, add_qa_to_chat

# Main function to handle a user's incoming chat request
def process_chat(question: str, chat_id: str = None):
    # Step 1: Send the question to Groq and get the AI's answer
    answer = get_llm_response(question)
    
    # Step 2: Check if this is a brand new conversation (no chat_id provided or default swagger value)
    if not chat_id or chat_id == "string":
        # Create a title using the first 30 characters of the question
        title = question[:30] + "..." if len(question) > 30 else question
        # Save a new chat session to the database and get its new ID
        chat_id = create_chat(title)
        
    # Step 3: Save the actual question and answer to the database, linking it to the chat
    qa_id = add_qa_to_chat(chat_id, question, answer)
    
    # Step 4: Return all the important info back to the API route
    return {
        "chat_id": chat_id, # The ID of the chat (so the frontend can continue the conversation later)
        "qa_id": qa_id, # The ID of this specific message pair
        "answer": answer # The actual text answer to display on the screen
    }
