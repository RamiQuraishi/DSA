"""
Data package for the Ontario Driving School Manager.
Contains database models, repositories, and session management.
"""

from .base import Base
from .session import SessionLocal, get_db
from .db_setup import init_db

__all__ = ['Base', 'SessionLocal', 'get_db', 'init_db'] 