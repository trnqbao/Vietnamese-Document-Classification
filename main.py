from fastapi import FastAPI
from pydantic import BaseModel
from gensim.models.doc2vec import Doc2Vec
from tensorflow.keras.models import load_model
from utils import load_stopwords, classify

app = FastAPI()

doc2vec = Doc2Vec.load('models/doc2vec.model')
model = load_model('models/doc2vec_nn_model.keras')
stopwords = load_stopwords('dataset/stopwords-vi.txt')

class Request(BaseModel):
    text: str

@app.post("/classify")
def classify(req: Request):
    label = classify(req.text, stopwords, doc2vec, model)
    return {"label": label}
