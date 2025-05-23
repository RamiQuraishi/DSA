"""
Student model for the Ontario Driving School Manager.
"""

from sqlalchemy import Column, String, Date, Boolean
from ontario_driving_school_manager.models.base import Base

class Student(Base):
    """
    Student model representing a driving school student.
    """
    __tablename__ = "students"
    
    # Personal Information
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    date_of_birth = Column(Date, nullable=False)
    
    # License Information
    license_number = Column(String(20), unique=True)
    license_class = Column(String(2))  # G1, G2, G
    
    # Status
    is_active = Column(Boolean, default=True)
    
    def __repr__(self) -> str:
        """String representation of the student."""
        return f"<Student {self.first_name} {self.last_name}>" 