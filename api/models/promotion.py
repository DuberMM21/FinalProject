from sqlalchemy import Column, Integer, String, Float, Boolean
from api.dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    discount = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
