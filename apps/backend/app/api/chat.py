from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.qa_service import answer_question

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
def chat_with_documents(payload: ChatRequest):
    result = answer_question(
        question=payload.question,
        document_ids=payload.document_ids,
    )

    return ChatResponse(**result)