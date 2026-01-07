-- Subject Data for Student Performance Dashboard
-- This file contains all subject records for the system

-- Insert sample subjects with proper course codes and instructor info
INSERT INTO subjects (name, code, instructor, credits, status) VALUES
('PYTHON', 'CS201', 'Dr. Abhishek', 4, 'Active'),
('OPERATING SYSTEM', 'CS202', 'Prof. Sharma', 4, 'Active'),
('DELD', 'CS203', 'Dr. Verma', 3, 'Active'),
('DSA', 'CS204', 'Dr. Kumar', 4, 'Active'),
('MATHEMATIC III', 'CS205', 'Prof. Singh', 3, 'Active')
ON CONFLICT (code) DO NOTHING;
