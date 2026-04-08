import numpy as np
from pyvi import ViTokenizer
from gensim.utils import simple_preprocess
from gensim.models.doc2vec import Doc2Vec
from tensorflow.keras.models import load_model

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return {line.strip() for line in f if line.strip()}

_stopwords = load_stopwords('dataset/stopwords-vi.txt')
_doc2vec = Doc2Vec.load('models/doc2vec.model')
_model = load_model('models/doc2vec_nn_model.keras')

def preprocess(doc, stopwords):
    tokenized_doc = ViTokenizer.tokenize(doc)
    tokens = simple_preprocess(tokenized_doc)
    tokens = [token for token in tokens if token not in stopwords]
    return " ".join(tokens)

def classify_doc(doc):
    doc = preprocess(doc, _stopwords)
    vector = _doc2vec.infer_vector(doc.split())
    vector = np.array(vector).reshape(1, -1)
    return _model.predict(vector)