"""HTTP data mappers."""
from common.docstring import MAPPER_DOCSTRING
from models.rag import ChatsModel, ConversationsModel
from .schema import ChatResponse, ConversationResponse

class ChatResponseMapper:
    @staticmethod
    def entityToResponse(instance: ChatsModel) -> ChatResponse:
        return ChatResponse(
            id=instance.id,
            chatRole=instance.chatRoleId,
            conversationId=instance.conversationId,
            messages=instance.message
        )

class ConversationResponseMapper:
    @staticmethod
    def entityToResponse(instance: ConversationsModel) -> ConversationResponse:
        return ConversationResponse(
            id=instance.id,
            name=instance.name,
            userId=instance.userId
        )