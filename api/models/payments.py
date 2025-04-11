from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    payment_type = Column(String(50), nullable=False)  #'card', 'cash'
    status = Column(String(20), nullable=False, default="pending")  #'pending', 'completed', 'failed'

    order = relationship("Order", back_populates="payment")
