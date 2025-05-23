"""
Database setup and initialization.
This module provides functions for database initialization and setup.
"""

import logging
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .base import Base
from .session import engine

logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize database by creating all tables.
    """
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except SQLAlchemyError as e:
        logger.error(f"Error creating database tables: {e}")
        raise

def check_db_connection() -> bool:
    """
    Check database connection.
    
    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError as e:
        logger.error(f"Database connection error: {e}")
        return False

def reset_db() -> None:
    """
    Reset database by dropping all tables and recreating them.
    """
    try:
        # Drop all tables
        Base.metadata.drop_all(bind=engine)
        logger.info("Database tables dropped successfully")
        
        # Recreate all tables
        init_db()
    except SQLAlchemyError as e:
        logger.error(f"Error resetting database: {e}")
        raise

def ensure_db_directory() -> None:
    """
    Ensure database directory exists.
    """
    db_path = Path("driving_school.db")
    if db_path.exists():
        return
    
    try:
        # Create parent directory if it doesn't exist
        db_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info("Database directory created successfully")
    except Exception as e:
        logger.error(f"Error creating database directory: {e}")
        raise