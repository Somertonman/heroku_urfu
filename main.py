from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
@app.post("/predict")
def read_root(request: Request):
  resp = request.body()
  classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
  result = classifier(resp)
  return result
  
  
@app.get("/predict")
def h():
  return "get works"



