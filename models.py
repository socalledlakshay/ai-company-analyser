from pydantic import BaseModel

class Company(BaseModel):
    name: str
    industry: str
    business_model: str
    products: list[str]
    competitors: list[str]