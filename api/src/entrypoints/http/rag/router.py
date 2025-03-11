"""HTTP route definitions."""

from fastapi import APIRouter, Path, UploadFile, File

from di.dependency_injection import injector
from di.unit_of_work import AbstractUnitOfWork
from usecases import chat_usecases as chatUsecases

from common.types import UUIDStr
from .schema import *
from .mapper import ChatResponseMapper, ConversationResponseMapper

router = APIRouter(prefix="/api/v1/chat")


@router.get("/{conversation_id}")
async def getChats(conversation_id: str = Path(..., __doc__=UUIDStr.__doc__)):
    """Get conversations content"""
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    chats = await chatUsecases.getChats(
        asyncUnitOfWork=asyncUnitOfWork, conversationId=conversation_id
    )

    result = list(map(ChatResponseMapper.entityToResponse, chats))
    return result


@router.get("/conversations/{user_id}")
async def getConversations(user_id: str = Path(..., __doc__=UUIDStr.__doc__)):
    """Get all conversation of a user"""
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    conversation = await chatUsecases.getConversations(
        asyncUnitOfWork=asyncUnitOfWork, userId=user_id
    )

    result = list(map(ConversationResponseMapper.entityToResponse, conversation))
    return result


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

