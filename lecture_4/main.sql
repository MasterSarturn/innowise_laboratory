-- Table: students
-- Stores information about each student
CREATE TABLE IF NOT EXISTS students
     (
    id INTEGER PRIMARY KEY autoincrement,
     full_name TEXT NOT NULL,
     birth_year integer NOT NULL);
-- Insert sample student data
insert into students (full_name, birth_year)
     values
     ('Alice Johnson', 2005),
     ('Brian Smith', 2004), 
     ('Carla Reyes', 2006),
     ('Daniel Kim', 2005),
     ('Eva Thompson', 2003),
     ('Felix Nguyen', 2007),
     ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);  
-- Table: grades
-- Stores grades for each student in different subjects
create table if not exists grades
     (
     id integer primary key autoincrement,
     student_id integer not null,
     subject text not null,
     grade integer not null check(grade >0 and grade <101), 
     foreign key(student_id) references students(id)
     );
-- Insert sample grade data
insert into grades (student_id, subject, grade)
                values
                (1, 'Math', 88),
                (1, 'English', 92),
                (1, 'Science', 85),
                (2, 'Math', 75),
                (2, 'History', 83),
                (2, 'English', 79),
                (3, 'Science', 95),
                (3, 'Math', 91),
                (3, 'Art', 89),
                (4, 'Math', 84),
                (4, 'Science', 88),
                (4, 'Physical Education', 93),
                (5, 'English', 90),
                (5, 'History', 85),
                (5, 'Math', 88),
                (6, 'Science', 72),
                (6, 'Math', 78),
                (6, 'English', 81),
                (7, 'Art', 94),
                (7, 'Science', 87),
                (7, 'Math', 90),
                (8, 'History', 77),
                (8, 'Math', 83),
                (8, 'Science', 80),
                (9, 'English', 96),
                (9, 'Math', 89),
                (9, 'Art', 92);
-- Index: speeds up join operations on grades(student_id)
create index if not exists idx_studg_id on grades (student_id);
-- Get all grades for student Alice Johnson
select g.grade from
students s inner join grades g
on s.id = g.student_id
where s.full_name = 'Alice Johnson';
-- Calculate the average grade for each student
select s.full_name, avg(g.grade) as avg_grade from
students s inner join grades g
on s.id = g.student_id
group by s.full_name;
-- List all students born after the year 2004
select s.full_name from students s
where birth_year >2004;
-- List each subject with its average grade
select g.subject, avg(g.grade) from
grades g
group by g.subject;
-- Find the top 3 students with the highest average grade
select s.full_name, avg(g.grade) as avg_grade
from students s inner join grades g
on s.id = g.student_id 
group by s.full_name
order by avg(g.grade) desc limit 3;
-- Show all students who have scored below 80
select distinct s.full_name
from students s inner join grades g
on s.id = g.student_id 
where g.grade <80;