import abc
from abc import abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstraction import AbstractRagRepository
from repositories.relational_db import RelationalDBRagRepository

T = TypeVar("T", bound=AbstractRagRepository)


class AbstractUnitOfWork(Generic[T], abc.ABC):
    ragRepo: AbstractRagRepository

    def __init__(self, ragRepo: T):
        self.ragRepo = ragRepo

    @abstractmethod
    async def __aenter__(self) -> "AbstractUnitOfWork":
        raise NotImplemented

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplemented


class AsyncSQLAlchemyUnitOfWork(AbstractUnitOfWork[RelationalDBRagRepository]):
    def __init__(
        self,
        session: AsyncSession,
        ragRepo: RelationalDBRagRepository,
    ):
        super().__init__(ragRepo=ragRepo)
        self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Any,
    ):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()
            await self.remove()

    async def remove(self):
        from settings.db import AsyncScopedSession

        await AsyncScopedSession.remove()
