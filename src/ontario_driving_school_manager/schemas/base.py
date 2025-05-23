"""
Base schema for the Ontario Driving School Manager.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Base Pydantic model for all schemas.
    Provides common functionality and attributes.
    """
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None 