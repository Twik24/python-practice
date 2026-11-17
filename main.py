
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scoring import analyse

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.get("/hello")
def hello():
    return({"message": "Yoo wagwann"})


class ScoreInput(BaseModel):
    scores: list[int]

@app.post("/analyse")
def analyse_scores(data: ScoreInput):
    if len(data.scores) == 0:
        raise HTTPException(status_code=400, detail="Provide at least one score.")
    return analyse(data.scores)