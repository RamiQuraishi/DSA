"""
Logging utilities for the Ontario Driving School Manager.
"""

import logging
import logging.config
import sys
from pathlib import Path
from typing import Optional

import yaml

def setup_logging(
    config_file: Optional[str] = None,
    default_level: int = logging.INFO
) -> None:
    """
    Set up logging configuration from YAML file.
    
    Args:
        config_file: Path to YAML config file. If None, uses default config.
        default_level: Default logging level if config file is not found.
    """
    if config_file:
        config_path = Path(config_file)
        if config_path.exists():
            with open(config_path) as f:
                config = yaml.safe_load(f)
                logging.config.dictConfig(config)
                return

    # Fallback to basic configuration if config file not found
    logging.basicConfig(
        level=default_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Set specific logger levels for third-party libraries
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("alembic").setLevel(logging.WARNING) 