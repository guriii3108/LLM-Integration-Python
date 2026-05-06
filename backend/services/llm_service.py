# Import the official Groq client library
from groq import Groq
# Import our settings to securely access the GROQ API key
from config.settings import settings

# Initialize the Groq client with our API key
client = Groq(api_key=settings.GROQ_API_KEY)

# Define a function that takes a question string and returns an answer string
def get_llm_response(question: str) -> str:
    try:
        # Call the Groq chat completions API
        response = client.chat.completions.create(
            # Specify the specific AI model to use (Updated to llama-3.1-8b-instant since older one was decommissioned)
            model="llama-3.1-8b-instant",
            # Pass the user's question inside the messages array
            messages=[
                {"role": "user", "content": question}
            ]
        )
        # Extract and return only the text content from the AI's response
        return response.choices[0].message.content
    except Exception as e:
        # If something goes wrong (like a bad API key or no internet), print the error
        print(f"Error calling Groq API: {e}")
        # Return a fallback message so the frontend doesn't crash completely
        return "I'm sorry, I am currently unavailable."
