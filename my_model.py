import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)

def gemini_response(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=(
                "You are Jarvis, a witty, helpful, and friendly AI assistant. "
                "Reply to the user's question in an engaging, short and sweet way, as if you're chatting casually.\n\n"
                f"User: {user_input}\n"
                f"Jarvis:"
            ),
        )
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return "Oops, I had a brain freeze. Could you say that again?"
    
print(gemini_response("who is MS Dhoni?"))