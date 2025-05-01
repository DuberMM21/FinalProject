from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_status = Column(String(20), nullable=False, server_default="pending")
    payment_status = Column(String(20), nullable=False, server_default="unpaid")
    delivery_type = Column(String(20), nullable=False, server_default="pickup")
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    customer = relationship("User", back_populates="orders")
    reviews = relationship("Review", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
    promotion = relationship("Promotion", back_populates="order")