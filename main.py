from json_writer import save_json
from models import Company
from gemini_client import extract_company_profile
from extraction import create_company_profile

company_text = input(
    "Enter company text: "
)

try:
    response = extract_company_profile(company_text)
    company = create_company_profile(response)
    save_json(company.model_dump(), "company.json")
    print("Report saved successfully")

except Exception as e:
    print("Something went wrong:", e)