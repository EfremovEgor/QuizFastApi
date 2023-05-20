from pydantic import BaseModel
from datetime import datetime


class BaseQuestion(BaseModel):
    question_text: str
    answer_text: str


class QuestionCreate(BaseQuestion):
    ...


class QuestionReturn(BaseQuestion):
    id: int
    creation_date: datetime
