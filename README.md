# Vietnamese Document Classification

A deep learning-based system for classifying Vietnamese documents into 10 categories, powered by **Doc2Vec** embeddings and a **Neural Network** classifier, served via a **FastAPI** REST API.

---

## Categories

The model classifies documents into the following 10 labels:

| Label |
|---|
| Chính Trị |
| Đời Sống |
| Khoa Học |
| Kinh Doanh |
| Pháp Luật |
| Sức Khỏe |
| Thế Giới |
| Thể Thao |
| Văn Hóa |
| Công Nghệ |

### Dataset Distribution

![Label Distribution](assets/label_distribution.png)

---

## Model Architecture

### Pipeline
```
Raw Text → Preprocessing → Doc2Vec Embedding → Neural Network → Label
```

### Components

**Preprocessing**
- Vietnamese tokenization using `pyvi`
- Lowercasing and stopword removal

**Embedding**
- Doc2Vec model trained on the Vietnamese document corpus
- Converts each document into a dense vector representation

**Classifier**
- Neural Network trained on Doc2Vec vectors
- Output: probability distribution over 10 categories

### Training History

![Loss History](assets/loss_history.png)
![Accuracy History](assets/accuracy_history.png)

---

## API Usage

### Requirements

```bash
uv add fastapi uvicorn gensim tensorflow numpy pyvi
```

### Run the server

```bash
uv run uvicorn main:app --reload
```

### Endpoint

```
POST /classify
```

**Request body:**
```json
{
  "text": "Lãi suất vay mượn giữa các ngân hàng nhiều phiên tăng mạnh và được dự báo khó sớm quay về mức thấp như trước. Từ đầu năm đến nay, lãi suất trên thị trường liên ngân hàng biến động mạnh. Phiên 4/2, lãi suất qua đêm vọt lên 17%, mức cao nhất trong khoảng một thập kỷ. Trong tháng 3, thị trường ghi nhận nhiều phiên lãi suất vượt 10% trước khi hạ nhiệt. Đến đầu tháng 4, lãi suất qua đêm vẫn duy trì quanh 9%."
}
```

**Response:**
```json
{
  "index": 1,
  "label": "Kinh Doanh",
  "confidence": 0.8131
}
```

### Interactive Docs

FastAPI provides a built-in Swagger UI at:
```
http://127.0.0.1:8000/docs
```

---

## Project Structure

```
vietnamese-document-classification/
├── assets/...
├── datasets/...
├── models/...
├── Training Pipeline.ipynb
├── schemas.py
├── utils.py
├── main.py
└── README.md
```
