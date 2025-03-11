from typing import Any, Tuple
from common.utils import build_uuid4_str
from common.types import UUIDStr

from di.unit_of_work import AbstractUnitOfWork
from models.rag import *


async def getConversations(
    asyncUnitOfWork: AbstractUnitOfWork,
    userId: UUIDStr,
    params: Optional[GetConversationsParamsModel] = None,
) -> list[ConversationsModel]:
    async with asyncUnitOfWork as auow:
        return await auow.ragRepo.getConversation(userId=userId, params=params)


async def getChats(
    asyncUnitOfWork: AbstractUnitOfWork,
    conversationId: UUIDStr,
    params: Optional[GetChatsParamsModel] = None,
) -> list[ChatsModel]:
    async with asyncUnitOfWork as auow:
        return await auow.ragRepo.getChats(conversationId=conversationId, params=params)


async def createChat(
    asyncUnitOfWork: AbstractUnitOfWork, input: CreateChatsModel
) -> str:
    async with asyncUnitOfWork as auow:
        chats = await auow.ragRepo.getChats(conversationId=input.conversationId)
        is_new_conversation = not chats

        conversation_id = input.conversationId
        if is_new_conversation:
            conversation_id = await auow.ragRepo.createConversation(
                CreateConversationModel(
                    id=input.conversationId, name="New chat", userId=input.userId
                )
            )

        user_message = CreateChatsModel(
            chatRoleId=1, conversationId=conversation_id, message=input.message
        )
        await auow.ragRepo.createChat(data=user_message)

        # TODO: Generate answer using a proper approach
        response = "Xin chào"

        ai_message = CreateChatsModel(
            chatRoleId=2, conversationId=conversation_id, message=response
        )
        await auow.ragRepo.createChat(data=ai_message)

        if is_new_conversation:
            await auow.ragRepo.updateConversation(
                data=UpdateConversationModel(id=conversation_id, name="Xin chào")
            )

    return response
