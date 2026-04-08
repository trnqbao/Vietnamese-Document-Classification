import numpy as np
from pydantic import BaseModel

LABELS = ['Chính Trị', 'Đời Sống', 'Khoa Học', 'Kinh Doanh', 'Pháp Luật', 
          'Sức Khỏe', 'Thế Giới', 'Thể Thao', 'Văn Hóa', 'Công Nghệ']

class ClassifyRequest(BaseModel):
    text: str

class ClassifyResponse(BaseModel):
    index: int
    label: str
    confidence: float

    @classmethod
    def from_prediction(cls, pred: np.ndarray):
        pred_idx = int(np.argmax(pred[0]))
        return cls(
            index=pred_idx,
            label=LABELS[pred_idx],
            confidence=float(pred[0][pred_idx])
        )