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


select count(*)
from "Registration"."Course_Requisite" inner join "Registration"."Student_Courses_Completed" on
"Registration"."Student_Courses_Completed".subject = "Registration"."Course_Requisite".req_course_subject
and "Registration"."Student_Courses_Completed".course_number = "Registration"."Course_Requisite".req_course_number
where "Registration"."Course_Requisite".req_course_subject = 'CSC' 
and "Registration"."Course_Requisite".req_course_number = '111'
and "Registration"."Student_Courses_Completed".student_pin = '41236346';


truncate table "Registration"."Schedule";

select count(*)
from "Registration"."Schedule";
