from sqlalchemy import Column, Integer, String, Boolean
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
