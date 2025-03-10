"""Mapper between domain models and database models."""
from common.docstring import MAPPER_DOCSTRING
from models.rag import *

from .orm import *

class ConversationsMapper:
    @staticmethod
    def ormToEntity(conversations: Conversation) -> ConversationsModel:
        return ConversationsModel(
            id = conversations.id,
            name=conversations.name,
            userId=conversations.user_id
        )
    
class ChatsMapper:
    @staticmethod
    def ormToEntity(chats: ChatMessage) -> ChatsModel:
        return ChatsModel(
            id = chats.id,
            chatRoleId = chats.chat_role_id,
            conversationId=chats.conversation_id,
            message=chats.message
        )