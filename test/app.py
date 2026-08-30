from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="sum the two numbers")


class NumberPair(BaseModel):
    a: int
    b: int


@app.post("/add-numbers")
def add_numbers(payload: NumberPair):
    return {"result": payload.a + payload.b}