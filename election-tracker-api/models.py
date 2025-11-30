from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Politician(Base):
    __tablename__ = "politicians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    vote = Column(Integer, default=0)
    party = Column(String, nullable=False)
    area_id = Column(Integer, ForeignKey("constituencies.id"), nullable=False)
    
    # Relationship back to constituency
    constituency = relationship("Constituency", back_populates="candidates")


class Constituency(Base):
    __tablename__ = "constituencies"

    id = Column(Integer, primary_key=True, index=True)
    election_area = Column(String, nullable=False, unique=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationship to politicians (candidates)
    candidates = relationship("Politician", back_populates="constituency", order_by="desc(Politician.vote)")
