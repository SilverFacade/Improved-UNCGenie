insert into "Registration"."Person" (pin, first_name, last_name, password, address, email, phone_number)
values 
	('98513241', 'Rosie', 'Delacruz', '327914', '1234 Example St', 'RD@gmail.com', '000-000-0000'),
	('41236346', 'Jorge', 'Erickson', '616435', '1234 Example St', 'GE@gmail.com', '000-000-0000'),
	('93428713', 'Roger', 'Sykes', '157456', '1234 Example St', 'RS@gmail.com', '000-000-0000'),
	('32187189', 'Jenson', 'White', '613447', '1234 Example St', 'JW@gmail.com', '000-000-0000'),
	('14269834', 'Wanda', 'Gallegos', '153453', '1234 Example St', 'WG@gmail.com', '000-000-0000'),
	('32107423', 'Lulu', 'Poole', '163465', '1234 Example St', 'LP@gmail.com', '000-000-0000');


insert into "Registration"."Student" (pin, year, emergency_contact)
values 
	('98513241', 'Senior', '111-111-1111'),
	('41236346', 'Senior', '111-111-1111'),
	('32187189', 'Junior', '111-111-1111'),
	('32107423', 'Senior', '111-111-1111');


insert into "Registration"."Instructor" (pin, department)
values 
	('93428713', 'Math'),
	('14269834', 'Computer Science');


insert into "Registration"."Course" (subject, course_number, title, credits, description)
values 
	('MAT', '111', 'Math1', 3, 'Math1 is introductory math .............................
	....................................................................................
	....................................................................................'),
	('MAT', '222', 'Math2', 4, 'Math2 is intermediate level math .............................
	....................................................................................
	....................................................................................'),
	('MAT', '333', 'Math3', 3, 'Math3 is advanced math .............................
	....................................................................................
	....................................................................................'),
	('CSC', '111', 'Com1', 3, 'Com1 is introductory computer science .............................
	....................................................................................
	....................................................................................'),
	('CSC', '222', 'Com2', 3, 'Com2 is intermediate level computer science .............................
	....................................................................................
	....................................................................................'),
	('CSC', '333', 'Com3', 4, 'Com1 is advanced computer science .............................
	....................................................................................
	....................................................................................');


insert into "Registration"."Section" (subject, course_number, section_number, crn, active,
									capacity, start_date, location, campus, days, 
									start_time, end_time, waitlist_active, waitlist_capacity, xl_active, 
									xl_capacity, attribute, instructor_pin)
values 
	('MAT', '111', '02', '13412', 25, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '222', '01', '41234', 4, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '12:00 PM', 
	'1:15 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '333', '01', '67312', 9, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00 AM', 
	'10:50 AM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '111', '01', '14729', 26, 28, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '222', '02', '14729', 26, 28, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '333', '02', '14729', 26, 28, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '14269834');


insert into "Registration"."Course_Requisite" (subject, course_number, req_course_subject,
											req_course_number, prerequisite, corequisite)
values 
	('MAT', '222', 'MAT', '111', true, false),
	('MAT', '333', 'MAT', '222', true, false),
	('CSC', '222', 'CSC', '111', true, false),
	('CSC', '333', 'CSC', '222', true, false);


insert into "Registration"."Major" (major_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Chemistry'),
	('French'),
	('Business');


insert into "Registration"."Minor" (minor_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Chemistry'),
	('French'),
	('Business');


insert into "Registration"."Student_Major" (student_pin, major_name)
values 
	('98513241', 'Computer Science'),
	('41236346', 'Computer Science'),
	('32187189', 'Math'),
	('32107423', 'Math');


insert into "Registration"."Student_Minor" (student_pin, minor_name)
values 
	('98513241', 'Biology'),
	('41236346', 'Math'),
	('32187189', 'Computer Science'),
	('32107423', 'Business');


insert into "Registration"."Major_Courses" (major_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '222'),
	('Computer Science', 'CSC', '333'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '222'),
	('Math', 'MAT', '333');


insert into "Registration"."Minor_Courses" (minor_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '222'),
	('Computer Science', 'CSC', '333'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '222'),
	('Math', 'MAT', '333');


insert into "Registration"."Student_Courses_Completed" (student_pin, subject, course_number)
values 
	('98513241', 'MAT', '111'),
	('98513241', 'MAT', '222'),
	('41236346', 'CSC', '111'),
	('41236346', 'MAT', '111'),
	('41236346', 'MAT', '222');


























	
