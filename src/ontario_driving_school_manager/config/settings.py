"""
Settings management for the Ontario Driving School Manager.
"""

import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    # Application
    APP_NAME: str = "Ontario Driving School Manager"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "sqlite:///./driving_school.db"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # UI
    WINDOW_WIDTH: int = 1200
    WINDOW_HEIGHT: int = 800
    THEME: str = "light"

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True

def load_settings() -> Dict[str, Any]:
    """
    Load application settings from environment variables and .env file.
    
    Returns:
        Dict[str, Any]: Dictionary containing application settings
    """
    # Load environment variables from .env file
    env_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(env_path)

    # Create settings instance
    settings = Settings()
    
    # Convert to dictionary
    return settings.dict() 