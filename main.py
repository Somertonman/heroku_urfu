from fastapi import FastAPI
from transformers import pipeline


app = FastAPI()
@app.get("/{input_str}")
def read_root():
  classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
  result = classifier(input_str)
  return result
  
  
  


