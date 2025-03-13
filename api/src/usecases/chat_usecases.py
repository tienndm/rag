from typing import Any, Tuple, Optional
from common.utils import build_uuid4_str
from common.types import UUIDStr
from common.logging import SingletonLogger

from di.unit_of_work import AbstractUnitOfWork
from models.rag import *

logger = SingletonLogger.getLogger()


async def getConversations(
    asyncUnitOfWork: AbstractUnitOfWork,
    userId: UUIDStr,
    params: Optional[GetConversationsParamsModel] = None,
) -> list[ConversationsModel]:
    logger.info(
        f"#chat_usecases.getConversations - get conversations - userId: {userId}, params: {params}"
    )
    try:
        async with asyncUnitOfWork as auow:
            return await auow.ragRepo.getConversation(userId=userId, params=params)
    except Exception as e:
        logger.error(
            f"#chat_usecases.getConversations - get conversations - error: {str(e)}"
        )
        raise


async def getChats(
    asyncUnitOfWork: AbstractUnitOfWork,
    conversationId: UUIDStr,
    params: Optional[GetChatsParamsModel] = None,
) -> list[ChatsModel]:
    logger.info(
        f"#chat_usecases.getChats - get chats - conversationId: {conversationId}, params: {params}"
    )
    try:
        async with asyncUnitOfWork as auow:
            return await auow.ragRepo.getChats(
                conversationId=conversationId, params=params
            )
    except Exception as e:
        logger.error(f"#chat_usecases.getConversations - get chats - error: {str(e)}")
        raise


async def createChat(
    asyncUnitOfWork: AbstractUnitOfWork, input: CreateChatsModel
) -> str:
    logger.info(f"#chat_usecases.createChat - creat chat - input: {input}")
    try:
        async with asyncUnitOfWork as auow:
            chats = await auow.ragRepo.getChats(conversationId=input.conversationId)
            isNewConversation = not chats

            if isNewConversation:
                conversationId = await auow.ragRepo.createConversation(
                    CreateConversationModel(
                        id=input.conversationId, name="New chat", userId=input.userId
                    )
                )
            else:
                conversationId = input.conversationId

            userMessage = CreateChatsModel(
                chatRoleId=1, conversationId=conversationId, message=input.message
            )
            await auow.ragRepo.createChat(data=userMessage)

            # TODO: Generate answer using a proper approach
            response = "Xin chào"

            aiMessage = CreateChatsModel(
                chatRoleId=2, conversationId=conversationId, message=response
            )
            await auow.ragRepo.createChat(data=aiMessage)

            if isNewConversation:
                await auow.ragRepo.updateConversation(
                    data=UpdateConversationModel(id=conversationId, name="Xin chào")
                )

        return response
    except Exception as e:
        logger.error(f"#chat_usecases.createChat - create chat - error: {str(e)}")
        raise
