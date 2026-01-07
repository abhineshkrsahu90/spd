-- Create students table
CREATE TABLE IF NOT EXISTS students (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  department VARCHAR(100),
  gpa DECIMAL(3,2),
  attendance DECIMAL(5,2),
  activity_score DECIMAL(5,2),
  status VARCHAR(50) DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create subjects table
CREATE TABLE IF NOT EXISTS subjects (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  code VARCHAR(50) UNIQUE NOT NULL,
  instructor VARCHAR(255),
  credits INTEGER,
  status VARCHAR(50) DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create exams table
CREATE TABLE IF NOT EXISTS exams (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  exam_date DATE NOT NULL,
  exam_time TIME,
  duration VARCHAR(50),
  room VARCHAR(100),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Enable Row Level Security
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
ALTER TABLE subjects ENABLE ROW LEVEL SECURITY;
ALTER TABLE exams ENABLE ROW LEVEL SECURITY;

-- Allow public read/write for demo (change in production!)
CREATE POLICY "Enable read access for all" ON students FOR SELECT USING (true);
CREATE POLICY "Enable insert for all" ON students FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable update for all" ON students FOR UPDATE USING (true);
CREATE POLICY "Enable delete for all" ON students FOR DELETE USING (true);

CREATE POLICY "Enable read access for all" ON subjects FOR SELECT USING (true);
CREATE POLICY "Enable insert for all" ON subjects FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable update for all" ON subjects FOR UPDATE USING (true);
CREATE POLICY "Enable delete for all" ON subjects FOR DELETE USING (true);

CREATE POLICY "Enable read access for all" ON exams FOR SELECT USING (true);
CREATE POLICY "Enable insert for all" ON exams FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable update for all" ON exams FOR UPDATE USING (true);
CREATE POLICY "Enable delete for all" ON exams FOR DELETE USING (true);