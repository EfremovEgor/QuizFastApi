from fastapi import FastAPI, Depends
from typing import Any
from .schemas import BaseQuestion, QuestionCreate, QuestionReturn
from sqlalchemy.orm import Session
from .database import get_db
from .models import Question
import requests
import time
from fastapi.responses import JSONResponse

app = FastAPI()


def get_unique_external_data(questions_num: int, db: Session) -> list | None:
    data = requests.get(
        url=f"https://jservice.io/api/random?count={questions_num}"
    ).json()
    if data is None:
        return data

    to_save = list()
    for question in data:
        while (
            db.query(Question)
            .filter(Question.question_text == question["question"])
            .first()
            is not None
        ):
            question = requests.get(
                url=f"https://jservice.io/api/random?count=1"
            ).json()[0]
            time.sleep(0.2)

        to_save.append(
            Question(question_text=question["question"], answer_text=question["answer"])
        )
    return to_save


@app.post("/", response_model=None)
def create(questions_num: int, db: Session = Depends(get_db)) -> QuestionReturn | None:
    to_save = get_unique_external_data(questions_num, db)
    if to_save is None:
        return None
    db.add_all(to_save)
    db.commit()
    db.refresh(to_save[-1])
    return to_save[-1]


@app.get("/", response_model=None)
def get_by_id(id: int, db: Session = Depends(get_db)) -> QuestionReturn | None:
    return db.query(Question).filter(Question.id == id).first()
