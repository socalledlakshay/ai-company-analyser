from google import genai
from google.genai import types
from prompt import COMPANY_ANALYST_PROMPT

from config import API_key

client = genai.Client(
    api_key=API_key
)

def extract_company_profile(text):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction=COMPANY_ANALYST_PROMPT,
            response_mime_type="application/json"
        )
    )
    
    return response.text