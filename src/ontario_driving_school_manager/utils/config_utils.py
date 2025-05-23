"""
Configuration utilities for the Ontario Driving School Manager.
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml

def load_config(config_file: Optional[str] = None) -> Dict[str, Any]:
    """
    Load configuration from file or environment variables.
    
    Args:
        config_file: Optional path to YAML config file
        
    Returns:
        Dict containing configuration values
    """
    config: Dict[str, Any] = {
        "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///./driving_school.db"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "LOG_FILE": os.getenv("LOG_FILE", "logs/app.log"),
    }

    # Load from config file if specified
    if config_file:
        config_path = Path(config_file)
        if config_path.exists():
            with open(config_path) as f:
                file_config = yaml.safe_load(f)
                if file_config:
                    config.update(file_config)

    return config

def save_config(config: Dict[str, Any], config_file: str) -> None:
    """
    Save configuration to YAML file.
    
    Args:
        config: Configuration dictionary
        config_file: Path to save config file
    """
    config_path = Path(config_file)
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False) 