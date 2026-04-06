import numpy as np
from pyvi import ViTokenizer
from gensim.utils import simple_preprocess

LABELS = ['Chính Trị', 'Đời Sống', 'Khoa Học', 'Kinh Doanh', 'Pháp Luật', 'Sức Khỏe', 'Thế Giới', 'Thể Thao', 'Văn Hóa', 'Công Nghệ']

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return {line.strip() for line in f if line.strip()}

def preprocess(doc, stopwords):
    tokenized_doc = ViTokenizer.tokenize(doc)
    tokens = simple_preprocess(tokenized_doc)
    tokens = [token for token in tokens if token not in stopwords]
    return " ".join(tokens)

def classify(doc, stopwords, doc2vec, model):
    doc = preprocess(doc, stopwords)
    vector = doc2vec.infer_vector(doc.split())
    vector = np.array(vector).reshape(1, -1)
    pred = model.predict(vector)
    pred_idx = np.argmax(pred[0])
    return LABELS[pred_idx]