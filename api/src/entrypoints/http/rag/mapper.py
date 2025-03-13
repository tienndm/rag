"""HTTP data mappers."""

from fastapi.responses import JSONResponse

from common.docstring import MAPPER_DOCSTRING
from models.rag import (
    ChatsModel,
    ConversationsModel,
    GetChatsParamsModel,
    GetConversationsParamsModel,
)


class ChatResponseMapper:
    @staticmethod
    def toDict(chat: ChatsModel) -> dict:
        """Convert a ChatsModel instance to a dictionary."""
        return {
            "id": chat.id,
            "chatRole": chat.chatRoleId,
            "conversationId": chat.conversationId,
            "messages": chat.message,
        }

    @staticmethod
    def entityToResponse(instance: list[ChatsModel]) -> JSONResponse:
        """Convert a list of ChatsModel instances to a JSONResponse."""
        chatDicts = [ChatResponseMapper.toDict(chat) for chat in instance]
        return JSONResponse(
            content={"code": 200, "description": "success", "data": chatDicts},
            status_code=200,
        )


class ConversationResponseMapper:
    @staticmethod
    def toDict(conversation: ConversationsModel) -> dict:
        return {
            "id": conversation.id,
            "name": conversation.name,
            "userId": conversation.userId,
        }

    @staticmethod
    def entityToResponse(instance: list[ConversationsModel]) -> JSONResponse:
        conversationDicts = [
            ConversationResponseMapper.toDict(conversation) for conversation in instance
        ]
        return JSONResponse(
            content={"code": 200, "description": "success", "data": conversationDicts},
            status_code=200,
        )


class GetChatParamsMapper:
    @staticmethod
    def inputToEntity(page: int, size: int) -> GetChatsParamsModel:
        return GetChatsParamsModel(page=page, size=size)


class GetConversationParamsMapper:
    @staticmethod
    def inputToEntity(page: int, size: int) -> GetConversationsParamsModel:
        return GetConversationsParamsModel(page=page, size=size)
