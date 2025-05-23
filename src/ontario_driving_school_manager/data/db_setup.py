"""
Database initialization and setup.
"""

import logging
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ontario_driving_school_manager.config.settings import load_settings
from ontario_driving_school_manager.data.base import Base

logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize the database.
    Creates all tables and sets up initial data if needed.
    """
    settings = load_settings()
    database_url = settings.get("DATABASE_URL", "sqlite:///./driving_school.db")

    # Create database directory if using SQLite
    if database_url.startswith("sqlite"):
        db_path = Path(database_url.replace("sqlite:///", ""))
        db_path.parent.mkdir(parents=True, exist_ok=True)

    # Create engine
    engine = create_engine(
        database_url,
        connect_args={"check_same_thread": False} if database_url.startswith("sqlite") else {}
    )

    # Create all tables
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")

    # Create session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Initialize with session
    with SessionLocal() as db:
        # Add any initial data setup here
        pass 