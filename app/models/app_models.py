from datetime import datetime
from app.configs.database import db
from sqlalchemy import Column, DateTime, Integer, String
from dataclasses import dataclass


@dataclass
class Lead(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: datetime
    last_visit: datetime
    visits: int

    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    phone = Column(String, nullable=True, unique=True)
    creation_date = Column(DateTime(), default=datetime.now(), nullable=True)
    last_visit = Column(DateTime(), default=datetime.now(), nullable=True)
    visits = Column(Integer, default=1, nullable=True)
