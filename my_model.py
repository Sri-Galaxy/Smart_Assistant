import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def gemini_response(user_input):
    try:
        prompt = (
            "You are Jarvis, a witty, helpful, and friendly AI assistant. "
            "Reply to the user's question in an engaging, short and sweet way, as if you're chatting casually.\n\n"
            f"User: {user_input}\n"
            f"Jarvis:"
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return "Oops, I had a brain freeze. Could you say that again?"