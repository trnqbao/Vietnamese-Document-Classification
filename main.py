from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import classify_doc
from schemas import ClassifyRequest, ClassifyResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/classify", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    pred = classify_doc(req.text)
    return ClassifyResponse.from_prediction(pred)
