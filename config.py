import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("GEMINI_API_KEY")

if not API_key:
    raise RuntimeError(
        "API key not found"
    )