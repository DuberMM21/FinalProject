from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reviewer_name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    approved = Column(Boolean, default=False)
