"""ORM models for RAG (Retrieval-Augmented Generation)."""

from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP, func, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

from common.types import UUIDStr
from common.utils import build_uuid4_str
from repositories.relational_db.user.orm import User


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    pass


class ChatRole(Base):
    """Model representing different roles in a chat (e.g., user, assistant, system)."""

    __tablename__ = "chat_role"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False)
    role: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )

    messages: Mapped[List["ChatMessage"]] = relationship(
        "ChatMessage", back_populates="role"
    )


class ChatMessage(Base):
    """Model representing individual chat messages."""

    __tablename__ = "chat_message"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False)
    chat_role_id: Mapped[int] = mapped_column(
        ForeignKey("chat_role.id"), nullable=False
    )
    conversation_id: Mapped[UUIDStr] = mapped_column(
        ForeignKey("conversation.id"), nullable=False
    )
    message: Mapped[str] = mapped_column("message", String(5196), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )

    role: Mapped["ChatRole"] = relationship("ChatRole", back_populates="messages")
    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages"
    )

    __table_args__ = (Index("idx_chat_message_conversation_id", "conversation_id"),)


class Conversation(Base):
    """Model representing a conversation thread."""

    __tablename__ = "conversation"

    id: Mapped[UUIDStr] = mapped_column(
        "id", String(32), primary_key=True, nullable=False, default=build_uuid4_str
    )
    name: Mapped[str] = mapped_column("name", String(256), nullable=False)
    user_id: Mapped[UUIDStr] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )

    user: Mapped["User"] = relationship("User", back_populates="conversations")
    messages: Mapped[List["ChatMessage"]] = relationship(
        "ChatMessage", back_populates="conversation"
    )

    __table_args__ = (Index("idx_conversation_user_id", "user_id"),)


class Document(Base):
    """Model for storing document references used in RAG.
    Note: Embeddings are stored in a separate VectorDB."""

    __tablename__ = "document"

    id: Mapped[UUIDStr] = mapped_column(
        "id", String(32), primary_key=True, default=build_uuid4_str
    )
    title: Mapped[str] = mapped_column("title", String(256), nullable=False)
    content: Mapped[str] = mapped_column("content", String, nullable=False)
    external_id: Mapped[str] = mapped_column(
        "external_id",
        String(256),
        nullable=True,
        comment="ID reference in the vector database",
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False
    )
