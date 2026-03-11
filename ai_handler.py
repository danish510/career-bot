import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def get_career_advice(user_input):

    prompt = f"""
    Kamu adalah penasihat karir untuk pelajar.

    Minat pengguna:
    {user_input}

    Berikan:
    1. 2-3 rekomendasi karir
    2. penjelasan singkat
    3. skill yang perlu dipelajari
    """

    response = model.generate_content(prompt)

    return response.text
