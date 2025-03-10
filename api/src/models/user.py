"""User domain models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from common.types import UUIDStr, HashPasswordType


@dataclass
class UserModel:
    id: UUIDStr
    name: str
    username: str
    email: str
    role_id: int
    created_at: datetime


@dataclass
class UserRoleModel:
    id: int
    role: str


@dataclass
class CreateUserModel:
    name: str
    username: str
    email: str
    password: str
    role_id: int = 1


@dataclass
class GetUsersParamsModel:
    page: int = 1
    size: int = 10


@dataclass
class UserCredentialModel:
    username: str
    password: str
