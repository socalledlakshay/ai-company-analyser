import json
from models import Company

def create_company_profile(response_text):
    data = json.loads(response_text)
    profile = Company(**data)
    return profile