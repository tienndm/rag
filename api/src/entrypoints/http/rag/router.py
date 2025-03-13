"""HTTP route definitions."""

from fastapi import APIRouter, Path, UploadFile, File
from typing import Optional

from di.dependency_injection import injector
from di.unit_of_work import AbstractUnitOfWork
from usecases import chat_usecases as chatUsecases

from common.types import UUIDStr
from .schema import *
from .mapper import (
    ChatResponseMapper,
    ConversationResponseMapper,
    GetChatParamsMapper,
    GetConversationParamsMapper,
)

router = APIRouter(prefix="/chat")


@router.get("/{conversation_id}")
async def getChats(
    conversation_id: str = Path(..., __doc__=UUIDStr.__doc__),
    page: Optional[int] = 1,
    size: Optional[int] = 10,
):
    """Get conversations content"""
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    params = GetChatParamsMapper.inputToEntity(page=page, size=size)
    chats = await chatUsecases.getChats(
        asyncUnitOfWork=asyncUnitOfWork, conversationId=conversation_id, params=params
    )

    return ChatResponseMapper.entityToResponse(chats)


@router.get("/conversations/{user_id}")
async def getConversations(
    user_id: str = Path(..., __doc__=UUIDStr.__doc__),
    page: Optional[int] = 1,
    size: Optional[int] = 10,
):
    """Get all conversation of a user"""
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    params = GetConversationParamsMapper.inputToEntity(page=page, size=size)
    conversation = await chatUsecases.getConversations(
        asyncUnitOfWork=asyncUnitOfWork, userId=user_id, params=params
    )

    return ConversationResponseMapper.entityToResponse(conversation)


@router.post("/uploadPDF")
def uploadPDF(file: UploadFile = File(...)):
    """Upload PDF for RAG"""
    raise NotImplementedError


@router.post("/core")
async def chat(input: ChatRequest) -> str:
    """Handle Chat"""
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    response = await chatUsecases.createChat(asyncUnitOfWork, input)

    return response
