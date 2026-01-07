#!/usr/bin/env python
"""
Initialize database tables and seed with sample data
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from database import db
from models.database_models import Student, Subject, StudentSubject

def init_and_seed():
    """Initialize database and add sample data"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()
        print("[OK] Tables created")
        
        # Add sample subjects
        if Subject.query.count() == 0:
            subjects = [
                Subject(name='Mathematics', description='Basic and advanced mathematical concepts'),
                Subject(name='Physics', description='Classical and modern physics'),
                Subject(name='Chemistry', description='Organic and inorganic chemistry'),
                Subject(name='English', description='Language and literature studies'),
                Subject(name='Computer Science', description='Programming and algorithms'),
            ]
            db.session.add_all(subjects)
            db.session.commit()
            print(f"[OK] Added {len(subjects)} subjects")
        
        # Add sample students
        if Student.query.count() == 0:
            students = [
                Student(
                    name='Rahul Sharma',
                    email='rahul.sharma@college.edu',
                    department='Computer Science',
                    gpa=3.8,
                    attendance=92,
                    activity_score=8.5,
                    status='Active'
                ),
                Student(
                    name='Priya Singh',
                    email='priya.singh@college.edu',
                    department='Computer Science',
                    gpa=3.6,
                    attendance=88,
                    activity_score=8.0,
                    status='Active'
                ),
                Student(
                    name='Aditya Patel',
                    email='aditya.patel@college.edu',
                    department='Computer Science',
                    gpa=3.2,
                    attendance=85,
                    activity_score=7.5,
                    status='Active'
                ),
                Student(
                    name='Neha Gupta',
                    email='neha.gupta@college.edu',
                    department='Computer Science',
                    gpa=3.9,
                    attendance=95,
                    activity_score=9.0,
                    status='Active'
                ),
                Student(
                    name='Vikram Kumar',
                    email='vikram.kumar@college.edu',
                    department='Computer Science',
                    gpa=2.8,
                    attendance=78,
                    activity_score=6.5,
                    status='Active'
                ),
                Student(
                    name='Ananya Verma',
                    email='ananya.verma@college.edu',
                    department='Computer Science',
                    gpa=3.5,
                    attendance=89,
                    activity_score=8.2,
                    status='Active'
                ),
                Student(
                    name='Rohan Singh',
                    email='rohan.singh@college.edu',
                    department='Computer Science',
                    gpa=3.1,
                    attendance=82,
                    activity_score=7.0,
                    status='Active'
                ),
                Student(
                    name='Divya Iyer',
                    email='divya.iyer@college.edu',
                    department='Computer Science',
                    gpa=3.7,
                    attendance=91,
                    activity_score=8.8,
                    status='Active'
                ),
            ]
            db.session.add_all(students)
            db.session.commit()
            print(f"[OK] Added {len(students)} students")
        
        print("\n[OK] Database initialization complete!")

if __name__ == '__main__':
    init_and_seed()
