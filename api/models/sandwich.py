from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    ingredients = Column(String(200))
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

    menu_id = Column(Integer, ForeignKey("menu.id"))
    menu = relationship("Menu", back_populates="sandwiches")
