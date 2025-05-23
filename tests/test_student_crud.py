"""
Test script for Student CRUD operations.
"""

from datetime import date
from sqlalchemy.orm import Session

from ontario_driving_school_manager.data.db_setup import init_db
from ontario_driving_school_manager.data.session import SessionLocal
from ontario_driving_school_manager.data.repositories.student import StudentRepository
from ontario_driving_school_manager.models.student import Student

def test_student_crud():
    """Test CRUD operations for Student model."""
    # Initialize database
    init_db()
    
    # Create a database session
    db: Session = SessionLocal()
    
    try:
        # Create repository
        student_repo = StudentRepository(Student, db)
        
        # Create a new student
        new_student = Student(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            date_of_birth=date(2000, 1, 1),
            license_number="G1234-567890-12345",
            license_class="G1",
            is_active=True
        )
        
        # Test CREATE
        print("\n1. Creating a new student...")
        created_student = student_repo.create(db, obj_in=new_student)
        print(f"Created student: {created_student}")
        
        # Test READ
        print("\n2. Reading the student...")
        student = student_repo.get(db, created_student.id)
        print(f"Retrieved student: {student}")
        
        # Test UPDATE
        print("\n3. Updating the student...")
        student.first_name = "Johnny"
        updated_student = student_repo.update(db, db_obj=student, obj_in=student)
        print(f"Updated student: {updated_student}")
        
        # Test custom queries
        print("\n4. Testing custom queries...")
        email_student = student_repo.get_by_email("john.doe@example.com")
        print(f"Student by email: {email_student}")
        
        active_students = student_repo.get_active_students()
        print(f"Active students: {len(active_students)}")
        
        # Test DELETE
        print("\n5. Deleting the student...")
        student_repo.delete(db, id=created_student.id)
        print("Student deleted")
        
        # Verify deletion
        deleted_student = student_repo.get(db, created_student.id)
        print(f"Student after deletion: {deleted_student}")
        
    finally:
        db.close()

if __name__ == "__main__":
    test_student_crud() 