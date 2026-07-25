from google import genai
from google.genai import types
from prompt import COMPANY_ANALYST_PROMPT

from config import API_key

client = genai.Client(
    api_key=API_key
)

def ask_gemini(user_prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=COMPANY_ANALYST_PROMPT
        )
    )
    return response.text