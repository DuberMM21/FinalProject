from sqlalchemy import Column, Integer, String, Boolean
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    ingredients = Column(String(200), nullable=False)
    instructions = Column(String(200), nullable=False)
    vegetarian = Column(Boolean, default=False)
