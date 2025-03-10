"""Utility functions."""
from uuid import uuid4
import bcrypt


def build_uuid4_str():
    return str(uuid4().hex)

def public_dict(object_):
    return {k: v for k, v in vars(object_).items() if not k.startswith('_')}

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password: The plain text password to hash
        
    Returns:
        str: The hashed password as a string
    """
    if isinstance(password, str):
        password = password.encode('utf-8')
        
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hash.
    
    Args:
        plain_password: The plain text password to check
        hashed_password: The hashed password to check against
        
    Returns:
        bool: True if the password matches, False otherwise
    """
    if isinstance(plain_password, str):
        plain_password = plain_password.encode('utf-8')
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
        
    return bcrypt.checkpw(plain_password, hashed_password)