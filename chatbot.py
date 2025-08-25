import os
import asyncio
from dotenv import load_dotenv
from groq import Groq
 
# -------------------------------
# Load API key from .env file
# -------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
 
# -------------------------------
# Initialize Groq client
# -------------------------------
client = Groq(api_key=api_key)
 
# -------------------------------
# Async function to get model response
# -------------------------------
async def chat_with_groq(prompt, model="llama3-70b-8192"):
    """
    Sends a prompt to the Groq model and returns the response.
 
    Args:
        prompt (str): User's message.
        model (str): Groq model to use (default: llama3-70b-8192).
 
    Returns:
        str: Model's reply.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error] {e}"
 
# -------------------------------
# Command-line chat loop
# -------------------------------
async def main():
    print("Groq Chatbot (type 'exit' to quit)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        response = await chat_with_groq(user_input)
        print("AI:", response, "\n")
 
# -------------------------------
# Start chatbot
# -------------------------------
if __name__ == "__main__":
    asyncio.run(main())