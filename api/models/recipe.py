from sqlalchemy import Column, Integer, String, Boolean
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    ingredients = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    vegetarian = Column(Boolean, default=False)
