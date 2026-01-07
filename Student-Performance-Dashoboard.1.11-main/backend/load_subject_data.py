#!/usr/bin/env python
"""
Import subjects from SUBJECT_DATA.sql file into the database
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from database import db
from models.database_models import Subject

def import_subjects_from_sql():
    """Import subjects from SQL file"""
    app = create_app()
    
    with app.app_context():
        # Define subjects data
        subjects_data = [
            {'name': 'PYTHON', 'description': 'Core mathematics course'},
            {'name': 'OPERATING SYSTEM', 'description': 'Physics course'},
            {'name': 'DELD', 'description': 'Chemistry course'},
            {'name': 'DSA', 'description': 'English language and literature'},
            {'name': 'MATHEMATIC III', 'description': 'Advanced mathematics course'},
        ]
        
        imported_count = 0
        
        for subject_data in subjects_data:
            # Check if subject already exists
            existing = Subject.query.filter_by(name=subject_data['name']).first()
            if not existing:
                subject = Subject(
                    name=subject_data['name'],
                    description=subject_data['description']
                )
                db.session.add(subject)
                imported_count += 1
                print(f"[OK] Added: {subject_data['name']}")
            else:
                print(f"[SKIP] Already exists: {subject_data['name']}")
        
        db.session.commit()
        print(f"\n[OK] Successfully imported {imported_count} subjects")
        
        # Show all subjects
        all_subjects = Subject.query.all()
        print(f"\nTotal subjects in database: {len(all_subjects)}")
        for s in all_subjects:
            print(f"  - {s.name}: {s.description}")

if __name__ == '__main__':
    import_subjects_from_sql()
