from pydantic import BaseModel
from typing import List, Optional


class UploadResponse(BaseModel):
    document_id: int
    filename: str
    status: str


class CitationOut(BaseModel):
    document_id: Optional[int]
    filename: str
    page: Optional[int]
    snippet: str


class ChatRequest(BaseModel):
    question: str
    document_ids: Optional[List[int]] = None


class ChatResponse(BaseModel):
    answer: str
    citations: List[CitationOut]
    confidence: str


class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: str
    correction: Optional[str] = None
    document_id: Optional[int] = None


class FeedbackResponse(BaseModel):
    message: str
    feedback_id: int


class SummaryRequest(BaseModel):
    document_id: int


class SummaryResponse(BaseModel):
    summary: str
    citations: List[CitationOut]