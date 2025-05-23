"""
Base repository with common CRUD operations.
This module provides a base repository class with common database operations.
"""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..base import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    """
    Base repository class with common CRUD operations.
    
    Args:
        model: SQLAlchemy model class
        db: Database session
    """
    
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db
    
    def get(self, id: int) -> Optional[ModelType]:
        """
        Get a single record by ID.
        
        Args:
            id: Record ID
            
        Returns:
            Optional[ModelType]: Record if found, None otherwise
        """
        return self.db.get(self.model, id)
    
    def get_all(self) -> List[ModelType]:
        """
        Get all records.
        
        Returns:
            List[ModelType]: List of records
        """
        stmt = select(self.model)
        return list(self.db.scalars(stmt).all())
    
    def create(self, obj_in: Dict[str, Any]) -> ModelType:
        """
        Create a new record.
        
        Args:
            obj_in: Dictionary with record data
            
        Returns:
            ModelType: Created record
        """
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def update(self, id: int, obj_in: Dict[str, Any]) -> Optional[ModelType]:
        """
        Update a record.
        
        Args:
            id: Record ID
            obj_in: Dictionary with record data
            
        Returns:
            Optional[ModelType]: Updated record if found, None otherwise
        """
        db_obj = self.get(id)
        if db_obj:
            for key, value in obj_in.items():
                setattr(db_obj, key, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj
    
    def delete(self, id: int) -> bool:
        """
        Delete a record.
        
        Args:
            id: Record ID
            
        Returns:
            bool: True if record was deleted, False otherwise
        """
        db_obj = self.get(id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False
    
    def exists(self, id: int) -> bool:
        """
        Check if a record exists.
        
        Args:
            id: Record ID
            
        Returns:
            bool: True if record exists, False otherwise
        """
        return self.get(id) is not None 