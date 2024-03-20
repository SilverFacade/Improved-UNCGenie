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



                   
                   
                    
                    
                    SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
                    "Registration"."Schedule".section_number, "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".time,"Registration"."Section".waitlist_active,
                    "Registration"."Section".waitlist_capacity, "Registration"."Person"."last_name",
                    "Registration"."Course"."title"
                    FROM "Registration"."Schedule" inner join "Registration"."Section" on 
                    "Registration"."Section".course_number = "Registration"."Schedule".course_number and 
                    "Registration"."Section".section_number = "Registration"."Schedule".section_number and 
                    "Registration"."Section".subject = "Registration"."Schedule".subject
                    left join "Registration"."Course" on
                    "Registration"."Section".course_number = "Registration"."Course".course_number and 
                    "Registration"."Section".subject = "Registration"."Course".subject
                    left join "Registration"."Person" on
                    "Registration"."Section".instructor_pin = "Registration"."Person".pin
                    WHERE student_pin = '98513241'