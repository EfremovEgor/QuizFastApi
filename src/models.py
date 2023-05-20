from sqlalchemy import String, Integer, DateTime
from sqlalchemy.sql.schema import Column
from .database import Base
from datetime import datetime


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
