from sqlalchemy import Boolean, Column, Integer, String
from .database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
    has_redirection = Column(Boolean)
