"""
Configuration package for the Ontario Driving School Manager.
"""

from .settings import load_settings
from .logging import setup_logging

__all__ = ['load_settings', 'setup_logging'] 