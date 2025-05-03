from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    sandwiches = relationship("Sandwich", back_populates="menu")
