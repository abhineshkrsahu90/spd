#!/usr/bin/env python
"""
Import subjects from CSV file into the database
"""

import sys
import os
import csv
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from database import db
from models.database_models import Subject

def import_subjects_from_csv(csv_file):
    """Import subjects from CSV file"""
    app = create_app()
    
    with app.app_context():
        imported_count = 0
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Check if subject already exists
                existing = Subject.query.filter_by(name=row['name']).first()
                if not existing:
                    subject = Subject(
                        name=row['name'],
                        description=row.get('description', '')
                    )
                    db.session.add(subject)
                    imported_count += 1
                    print(f"[OK] Added: {row['name']}")
                else:
                    print(f"[SKIP] Already exists: {row['name']}")
        
        db.session.commit()
        print(f"\n[OK] Successfully imported {imported_count} subjects")

if __name__ == '__main__':
    csv_file = r'c:\Users\abhin\Downloads\subjects_rows.csv'
    if os.path.exists(csv_file):
        import_subjects_from_csv(csv_file)
    else:
        print(f"[ERROR] CSV file not found: {csv_file}")
        sys.exit(1)
