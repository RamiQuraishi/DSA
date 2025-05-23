"""
Core package for the Ontario Driving School Manager.
Contains core functionality, exceptions, and event handling.
"""

from .exceptions import (
    BaseError,
    ValidationError,
    DatabaseError,
    NotFoundError,
    BusinessLogicError
)

from .events import (
    Event,
    EventHandler,
    EventBus
)

__all__ = [
    'BaseError',
    'ValidationError',
    'DatabaseError',
    'NotFoundError',
    'BusinessLogicError',
    'Event',
    'EventHandler',
    'EventBus'
] 