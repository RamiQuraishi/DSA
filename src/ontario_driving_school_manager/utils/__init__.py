"""
Utility package for the Ontario Driving School Manager.
Contains helper functions and utilities.
"""

from .logging_utils import setup_logging
from .config_utils import load_config

__all__ = ['setup_logging', 'load_config'] 