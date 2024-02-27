-- Example Queries

/*
 * Selects all records from Section table. Showing every section that students can enroll in
 */
select *
from "Registration"."Section";


/*
 * Selects Student Rosie's (from pin) sections on her "Rosie Schedule" schedule 
 * (she could have more than 1 schedule)
 */
select subject, course_number, section_number
from "Registration"."Schedule"
where student_pin = '98513241' and schedule_name = 'Rosie Schedule';


/*
 * 1. Check if a CSC 112 has requisites (it does, requisites is true)
 * 2. If true, list them from Course_Requisite table (can tell if co- or pre-requisite)
 * Can check Student_Courses_Completed to check if the student has completed the courses
 */
select requisites
from "Registration"."Course"
where subject = 'CSC' and course_number = '112';

select req_course_subject, req_course_number
from "Registration"."Course_Requisite"
where subject = 'CSC' and course_number = '112';

/*
 * degree progress: 120 credit hours needed for degree, certain courses need completed
 * 1. Get total credit hours completed by student with Student_Courses_Completed
 * and Course table
 * 2. Divide by total credit hours needed by major using Major_Courses and Course table 
 * (need to take into account electives and optional courses)
 */