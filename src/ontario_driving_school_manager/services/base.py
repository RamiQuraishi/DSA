"""
Base service class for the Ontario Driving School Manager.
"""

from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session

from ontario_driving_school_manager.core.exceptions import NotFoundError
from ontario_driving_school_manager.data.repositories.base import BaseRepository

ModelType = TypeVar("ModelType")

class BaseService(Generic[ModelType]):
    """
    Base class for all services.
    Provides common CRUD operations and business logic.
    """
    def __init__(self, repository: BaseRepository[ModelType]):
        self.repository = repository

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """Get a single record by ID."""
        obj = self.repository.get(db, id)
        if not obj:
            raise NotFoundError(f"Record with id {id} not found")
        return obj

    def get_all(self, db: Session) -> List[ModelType]:
        """Get all records."""
        return self.repository.get_all(db)

    def create(self, db: Session, obj_in: ModelType) -> ModelType:
        """Create a new record."""
        return self.repository.create(db, obj_in)

    def update(self, db: Session, db_obj: ModelType, obj_in: ModelType) -> ModelType:
        """Update an existing record."""
        return self.repository.update(db, db_obj, obj_in)

    def delete(self, db: Session, id: int) -> None:
        """Delete a record."""
        self.repository.delete(db, id) 