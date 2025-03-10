import re
from datetime import datetime

class UUIDStr(str):
    """UUID represented as a hexadecimal string."""

    # regular expression to match 32 hexadecimal characters

    UUID_PATTERN = re.compile(r'^[a-fA-F0-9]{32}$')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)

        if not cls.UUID_PATTERN.match(instance):
            raise ValueError(f'\'{instance}\' is not a valid UUID hexadecimal string')

        return instance

class DateTime(str):
    """DateTime represented as a string with validation."""
    
    DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    def __new__(cls, value, format=DEFAULT_FORMAT):
        instance = super().__new__(cls, value)
        instance._format = format
        
        try:
            datetime.strptime(value, format)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid datetime string with format '{format}'")
        
        return instance
    
    @property
    def datetime(self):
        """Convert to Python datetime object."""
        return datetime.strptime(self, self._format)

class HashPasswordType(str):
    """Password hash represented as a string with validation."""
    
    # Common hash formats: bcrypt, argon2, sha256/512
    HASH_PATTERNS = [
        re.compile(r'^\$2[ayb]\$\d{2}\$[./A-Za-z0-9]{53}$'),  # bcrypt
        re.compile(r'^\$argon2i[d]?\$'),                      # argon2
        re.compile(r'^[a-fA-F0-9]{64}$'),                     # SHA-256
        re.compile(r'^[a-fA-F0-9]{128}$')                     # SHA-512
    ]
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        
        if not any(pattern.match(instance) for pattern in cls.HASH_PATTERNS):
            raise ValueError(f"'{instance[:10]}...' is not a valid password hash format")
        
        return instance
    
    def verify(self, password: str, verify_func=None) -> bool:
        """
        Verify if a password matches this hash.
        
        Args:
            password: The password to verify
            verify_func: A function that takes (password, hash) and returns boolean
                        If None, this method will return False
        
        Returns:
            bool: True if password matches the hash
        """
        if verify_func is None:
            raise ValueError("A verification function must be provided")
        return verify_func(password, self)