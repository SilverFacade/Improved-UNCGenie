/*
 * Inserts records into Person Table
 */
insert into "Registration"."Person" (pin, first_name, last_name, password, address, email, phone_number)
values 
	('98513241', 'Rosie', 'Delacruz', '327914', '1234 Example St', 'RD@gmail.com', '000-000-0000'),
	('41236346', 'Jorge', 'Erickson', '616435', '1234 Example St', 'GE@gmail.com', '000-000-0000'),
	('93428713', 'Roger', 'Roger Sykes', '157456', '1234 Example St', 'RS@gmail.com', '000-000-0000'),
	('32187189', 'Jenson', 'White', '613447', '1234 Example St', 'JW@gmail.com', '000-000-0000'),
	('14269834', 'Wanda', 'Gallegos', '153453', '1234 Example St', 'WG@gmail.com', '000-000-0000'),
	('32107423', 'Lulu', 'Poole', '163465', '1234 Example St', 'LP@gmail.com', '000-000-0000');


/*
 * Inserts records into Student Table
 */
insert into "Registration"."Student" (pin, year, emergency_contact)
values 
	('98513241', 'Senior', '111-111-1111'),
	('41236346', 'Senior', '111-111-1111'),
	('32187189', 'Junior', '111-111-1111'),
	('32107423', 'Senior', '111-111-1111');


/*
 * Inserts records into Instructor Table
 */
insert into "Registration"."Instructor" (pin, department)
values 
	('93428713', 'Math'),
	('14269834', 'Computer Science');


/*
 * Inserts records into Course Table
 */
insert into "Registration"."Course" (subject, course_number, title, credits, requisites)
values 
	('MAT', '111', 'Math1', 3, false),
	('MAT', '112', 'Math2', 4, true),
	('MAT', '113', 'Math3', 3, true),
	('CSC', '111', 'Com1', 3, false),
	('CSC', '112', 'Com2', 3, true),
	('CSC', '113', 'Com3', 4, true);


/*
 * Inserts records into Section Table
 */
insert into "Registration"."Section" (subject, course_number, section_number, crn, active,
									capacity, start_date, location, campus, days, 
									time, waitlist_active, waitlist_capacity, xl_active, 
									xl_capacity, attribute, instructor_pin)
values 
	('MAT', '111', '02', '13412', 12, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '8:00-9:15am',
	0, 5, 0, 5, null, '93428713'),
	('MAT', '113', '01', '41234', 12, 30, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '12:00-1:15pm',
	0, 5, 0, 5, null, '93428713'),
	('CSC', '111', '01', '67312', 12, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00-10:50am',
	0, 5, 0, 5, null, '14269834'),
	('CSC', '112', '02', '14729', 12, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '2:00-3:15pm',
	0, 5, 0, 5, null, '14269834');

/*
 * Inserts into Course_Requisite Table
 */
insert into "Registration"."Course_Requisite" (subject, course_number, req_course_subject,
											req_course_number, prerequisite, corequisite)
values 
	('MAT', '112', 'MAT', '111', true, false),
	('MAT', '113', 'MAT', '112', true, false),
	('CSC', '112', 'CSC', '111', true, false),
	('CSC', '113', 'CSC', '112', true, false);


/*
 * Inserts records into Schedule Table
 */
insert into "Registration"."Schedule" (student_pin, schedule_name, subject, course_number, section_number)
values 
	('98513241', 'Rosie Schedule', 'CSC', '111', '01'),
	('98513241', 'Rosie Schedule', 'MAT', '113', '01'),
	('93428713', 'Roger Schedule', 'CSC', '112', '02'),
	('93428713', 'Roger Schedule', 'MAT', '113', '01');


/*
 * Inserts records into Major Table
 */
insert into "Registration"."Major" (major_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Chemistry'),
	('French'),
	('Business');


/*
 * Inserts records into Minor Table
 */
insert into "Registration"."Minor" (minor_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Chemistry'),
	('French'),
	('Business');


/*
 * Inserts records into Student_Major Table
 */
insert into "Registration"."Student_Major" (student_pin, major_name)
values 
	('98513241', 'Computer Science'),
	('41236346', 'Computer Science'),
	('32187189', 'Math'),
	('32107423', 'Math');


/*
 * Inserts records into Student_Minor Table
 */
insert into "Registration"."Student_Minor" (student_pin, minor_name)
values 
	('98513241', 'Biology'),
	('41236346', 'Math'),
	('32187189', 'Computer Science'),
	('32107423', 'Business');


/*
 * Inserts records into Major_Courses Table
 */
insert into "Registration"."Major_Courses" (major_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '112'),
	('Computer Science', 'CSC', '113'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '112'),
	('Math', 'MAT', '113');


/*
 * Inserts records into Minor_Courses Table (kept same as Major_Courses because of lack of courses)
 */
insert into "Registration"."Minor_Courses" (minor_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '112'),
	('Computer Science', 'CSC', '113'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '112'),
	('Math', 'MAT', '113');


/*
 * Inserts records into Student_Sections_Enrolled Table
 */
insert into "Registration"."Student_Sections_Registered" (student_pin, subject, course_number, section_number)
values 
	('98513241', 'CSC', '111', '01'),
	('98513241', 'MAT', '113', '01'),
	('41236346', 'CSC', '112', '02'),
	('41236346', 'MAT', '113', '01');


/*
 * Inserts records into Student_Courses_Completed Table
 */
insert into "Registration"."Student_Courses_Completed" (student_pin, subject, course_number)
values 
	('98513241', 'MAT', '111'),
	('98513241', 'MAT', '112'),
	('41236346', 'CSC', '111'),
	('41236346', 'MAT', '111'),
	('41236346', 'MAT', '112');


























	
