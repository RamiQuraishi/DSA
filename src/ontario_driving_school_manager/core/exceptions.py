"""
Custom exceptions for the Ontario Driving School Manager.
"""

class BaseError(Exception):
    """Base exception class for all custom exceptions."""
    def __init__(self, message: str, *args):
        self.message = message
        super().__init__(message, *args)

class ValidationError(BaseError):
    """Raised when data validation fails."""
    pass

class DatabaseError(BaseError):
    """Raised when database operations fail."""
    pass

class NotFoundError(BaseError):
    """Raised when a requested resource is not found."""
    pass

class BusinessLogicError(BaseError):
    """Raised when business logic rules are violated."""
    pass 