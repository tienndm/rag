"""Mapper between user domain models and database models."""
from common.docstring import MAPPER_DOCSTRING
from models.user import *

from .orm import *

class UserMapper:
    """Maps between User ORM models and domain entities."""
    
    @staticmethod
    def ormToEntity(user: User) -> UserModel:
        """Convert ORM User to domain UserModel."""
        return UserModel(
            id=user.id,
            name=user.name,
            username=user.username,
            email=user.email,
            role_id=user.role_id,
            created_at=user.created_at
        )
    

class UserRoleMapper:
    """Maps between UserRole ORM models and domain entities."""
    
    @staticmethod
    def ormToEntity(role: UserRole) -> UserRoleModel:
        """Convert ORM UserRole to domain UserRoleModel."""
        return UserRoleModel(
            id=role.id,
            role=role.role
        )