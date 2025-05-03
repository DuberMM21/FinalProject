from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    description: str
    ingredients: str
    instructions: str
    vegetarian: bool

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        from_attributes = True
