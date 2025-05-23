"""
Student repository for the Ontario Driving School Manager.
"""

from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session

from ontario_driving_school_manager.data.repositories.base import BaseRepository
from ontario_driving_school_manager.models.student import Student

class StudentRepository(BaseRepository[Student]):
    """
    Repository for Student model operations.
    """
    def __init__(self, model: type[Student], db: Session):
        super().__init__(model, db)
    
    def get_by_email(self, email: str) -> Optional[Student]:
        """Get a student by email."""
        return self.db.query(Student).filter(Student.email == email).first()
    
    def get_by_license_number(self, license_number: str) -> Optional[Student]:
        """Get a student by license number."""
        return self.db.query(Student).filter(Student.license_number == license_number).first()
    
    def get_active_students(self) -> List[Student]:
        """Get all active students."""
        return self.db.query(Student).filter(Student.is_active == True).all()
    
    def search_by_name(self, name: str) -> List[Student]:
        """Search students by name (first or last)."""
        return self.db.query(Student).filter(
            (Student.first_name.ilike(f"%{name}%")) |
            (Student.last_name.ilike(f"%{name}%"))
        ).all() 