from pydantic import BaseModel, Field

class Company(BaseModel):
    name: str
    industry: str | None = None
    business_model: str | None = None
    products: list[str] = Field(default_factory=list)
    competitors: list[str] = Field(default_factory=list)