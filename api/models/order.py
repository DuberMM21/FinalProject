from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    description = Column(String)
