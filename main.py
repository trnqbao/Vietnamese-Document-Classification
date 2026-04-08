from fastapi import FastAPI
from utils import classify_doc
from schemas import ClassifyRequest, ClassifyResponse

app = FastAPI()

@app.post("/classify", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    pred = classify_doc(req.text)
    return ClassifyResponse.from_prediction(pred)
