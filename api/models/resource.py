from sqlalchemy import Column, Integer, String, Boolean
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    quantity = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
