from gemini_client import ask_gemini
from json_writer import save_json
import json
from models import Company

company = input(
    "Enter company name: "
)

try:
    response = ask_gemini(company)
    data = json.loads(response)
    company = Company(**data)
    save_json(company.model_dump(), "company.json")
    print("Report saved successfully")

except Exception as e:
    print("Something went wrong:", e)