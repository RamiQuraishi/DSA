"""
Base schema functionality.
This module provides common functionality for all Pydantic schemas.
"""

from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

class BaseSchema(BaseModel):
    """Base class for all schemas."""
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_encoders={
            datetime: lambda dt: dt.isoformat()
        }
    )

class BaseCreateSchema(BaseSchema):
    """Base class for create schemas."""
    pass

class BaseUpdateSchema(BaseSchema):
    """Base class for update schemas."""
    pass

class BaseInDBBaseSchema(BaseSchema):
    """Base class for database schemas."""
    
    id: int = Field(..., description="Record ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert schema instance to dictionary."""
        return self.model_dump()
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseInDBBaseSchema":
        """Create schema instance from dictionary."""
        return cls(**data) 