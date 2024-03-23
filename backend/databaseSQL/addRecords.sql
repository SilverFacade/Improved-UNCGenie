/*
*
*	Space For Comments 
*
*/



insert into "Registration"."Person" (pin, first_name, last_name, password, address, email, phone_number)
values 
	('98513241', 'Rosie', 'Delacruz', '327914', '1234 Example St', 'RD@email.com', '000-000-0000'),
	('41236346', 'Jorge', 'Erickson', '616435', '1234 Example St', 'GE@email.com', '000-000-0000'),
	('93428713', 'Roger', 'Sykes', '157456', '1234 Example St', 'RS@email.com', '000-000-0000'),
	('32187189', 'Jenson', 'White', '613447', '1234 Example St', 'JW@email.com', '000-000-0000'),
	('14269834', 'Wanda', 'Gallegos', '153453', '1234 Example St', 'WG@email.com', '000-000-0000'),
	('32196871', 'Jeff', 'Garrett', '338561', '1234 Example St', 'JG@email.com', '000-000-0000'),	
	('29776353', 'Iva', 'Harrison', '917692', '1234 Example St', 'IH@email.com', '000-000-0000'),
	('83678572', 'Antoinette', 'Butler', '987132', '1234 Example St', 'AB@email.com', '000-000-0000'),
	('48298615', 'Naomi', 'Wu', '612379', '1234 Example St', 'NW@email.com', '000-000-0000'),	
	('10986523', 'Harley', 'Navarro', '159732', '1234 Example St', 'HN@email.com', '000-000-0000'),
	('32107423', 'Lulu', 'Poole', '163465', '1234 Example St', 'LP@email.com', '000-000-0000');


insert into "Registration"."Student" (pin, year, emergency_contact)
values 
	('98513241', 'Junior', '111-111-1111'),
	('41236346', 'Freshman', '111-111-1111'),
	('32187189', 'Junior', '111-111-1111'),
	('32107423', 'Senior', '111-111-1111');


insert into "Registration"."Instructor" (pin, department)
values 
	('93428713', 'Math'),
	('32196871', 'History'),	
	('29776353', 'Philosophy'),
	('83678572', 'Biology'),
	('48298615', 'Physics'),	
	('10986523', 'French'),
	('14269834', 'Computer Science');


insert into "Registration"."Course" (subject, course_number, title, credits, description, si, wi, marker)
values 
	('MAT', '111', 'MathCourse1', 3, 'MathCourse1 is introductory math .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('MAT', '222', 'MathCourse2', 4, 'MathCourse2 is intermediate level math .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('MAT', '333', 'MathCourse3', 3, 'MathCourse3 is advanced math .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('MAT', '444', 'MathCourse4', 3, 'MathCourse4 is the final math course .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('CSC', '111', 'CSCourse1', 3, 'CSCourse1 is introductory computer science .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('CSC', '222', 'CSCourse2', 3, 'CSCourse2 is intermediate level computer science .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('CSC', '333', 'CSCourse3', 4, 'CSCourse3 is advanced computer science .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('CSC', '444', 'CSCourse4', 4, 'CSCourse4 is the final computer science course .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('PHI', '111', 'PhilosophyCourse1', 3, 'PhilosophyCourse1 is introductory Philosophy .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('PHI', '222', 'PhilosophyCourse2', 3, 'PhilosophyCourse2 is intermediate level Philosophy .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('PHI', '333', 'PhilosophyCourse3', 4, 'PhilosophyCourse3 is advanced Philosophy .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('PHI', '444', 'PhilosophyCourse4', 4, 'PhilosophyCourse4 is the final Philosophy course.............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('HIS', '111', 'HistoryCourse1', 3, 'HistoryCourse1 is introductory History .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('HIS', '222', 'HistoryCourse2', 3, 'HistoryCourse2 is intermediate level History .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('HIS', '333', 'HistoryCourse3', 4, 'HistoryCourse3 is advanced History .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('HIS', '444', 'HistoryCourse4', 4, 'HistoryCourse4 is the final History course.............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('BIO', '111', 'BiologyCourse1', 3, 'BiologyCourse1 is introductory Biology .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('BIO', '222', 'BiologyCourse2', 3, 'BiologyCourse2 is intermediate level Biology .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('BIO', '333', 'BiologyCourse3', 4, 'BiologyCourse3 is advanced Biology .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('BIO', '444', 'BiologyCourse4', 4, 'BiologyCourse4 is the final Biology course.............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('PHY', '111', 'PhysicsCourse1', 3, 'PhysicsCourse1 is introductory Physics .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('PHY', '222', 'PhysicsCourse2', 3, 'PhysicsCourse2 is intermediate level Physics .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('PHY', '333', 'PhysicsCourse3', 4, 'PhysicsCourse3 is advanced Physics .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('PHY', '444', 'PhysicsCourse4', 4, 'PhysicsCourse4 is the final Physics course.............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('FRE', '111', 'FrenchCourse1', 3, 'FrenchCourse1 is introductory French .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('FRE', '222', 'FrenchCourse2', 3, 'FrenchCourse2 is intermediate level French .............................
	....................................................................................
	....................................................................................',
	false, false, null),
	('FRE', '333', 'FrenchCourse3', 4, 'FrenchCourse3 is advanced French .............................
	....................................................................................
	....................................................................................',
	true, true, null),
	('FRE', '444', 'FrenchCourse4', 4, 'FrenchCourse4 is the final French course.............................
	....................................................................................
	....................................................................................',
	true, true, null);


insert into "Registration"."Section" (subject, course_number, section_number, crn, active,
									capacity, start_date, location, campus, days, 
									start_time, end_time, waitlist_active, waitlist_capacity, xl_active, 
									xl_capacity, attribute, instructor_pin)
values 
	('MAT', '111', '02', '13412', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '111', '01', '97142', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '222', '01', '41234', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '12:00 PM', 
	'1:15 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '222', '02', '61275', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '333', '01', '67312', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00 AM', 
	'10:50 AM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '333', '02', '15243', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '444', '01', '98723', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '93428713'),
	('MAT', '444', '02', '75436', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '93428713'),
	('HIS', '111', '02', '42167', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '111', '01', '72556', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '222', '01', '17356', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '8:00 AM', 
	'8:50 AM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '222', '02', '91853', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '3:00 PM', 
	'4:15 PM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '333', '01', '79354', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00 AM', 
	'10:50 AM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '333', '02', '27891', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '12:00 PM', 
	'2:15 PM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '444', '01', '37518', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '32196871'),
	('HIS', '444', '02', '31867', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '10:00 AM', 
	'11:15 AM', 0, 5, 0, 5, null, '32196871'),
	('PHI', '111', '02', '51713', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '111', '01', '72455', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '222', '01', '91824', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '222', '02', '98471', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 AM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '333', '01', '15097', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '12:00 PM', 
	'12:50 PM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '333', '02', '19862', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '444', '01', '10862', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '3:00 PM', 
	'3:50 PM', 0, 5, 0, 5, null, '29776353'),
	('PHI', '444', '02', '15896', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '29776353'),
	('BIO', '111', '02', '64326', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '8:00 AM', 
	'8:50 AM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '111', '01', '57324', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '222', '01', '89732', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '222', '02', '32687', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '333', '01', '19872', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00 AM', 
	'10:50 AM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '333', '02', '89231', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '8:00 AM', 
	'8:50 AM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '444', '01', '41456', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '83678572'),
	('BIO', '444', '02', '97451', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '83678572'),
	('PHY', '111', '02', '65454', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'10:15 AM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '111', '01', '14907', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '222', '01', '14097', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '10:00 AM', 
	'11:15 AM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '222', '02', '19345', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '333', '01', '46514', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '8:00 AM', 
	'8:50 AM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '333', '02', '56167', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '444', '01', '14978', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '48298615'),
	('PHY', '444', '02', '23852', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '12:00 PM', 
	'12:50 PM', 0, 5, 0, 5, null, '48298615'),
	('FRE', '111', '02', '98713', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '1:00 PM', 
	'2:15 PM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '111', '01', '12535', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '3:00 PM', 
	'3:50 PM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '222', '01', '16456', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '222', '02', '56965', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'10:15 AM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '333', '01', '82715', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '10:00 AM', 
	'10:50 AM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '333', '02', '83647', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '444', '01', '38835', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '2:00 PM', 
	'3:15 PM', 0, 5, 0, 5, null, '10986523'),
	('FRE', '444', '02', '68714', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '8:00 AM', 
	'8:50 AM', 0, 5, 0, 5, null, '10986523'),
	('CSC', '111', '02', '89761', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'TTH', '10:00 AM', 
	'11:15 AM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '111', '01', '86423', 30, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '1:00 PM', 
	'1:50 PM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '222', '01', '13276', 0, 25, '2024-08-23', 'Room3', 'Greensboro Campus', 'TTH', '8:00 AM', 
	'9:15 AM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '222', '02', '12384', 0, 25, '2024-08-23', 'Room4', 'Greensboro Campus', 'TTH', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '333', '01', '78921', 0, 27, '2024-08-23', 'Room2', 'Greensboro Campus', 'MWF', '2:00 PM', 
	'2:50 PM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '333', '02', '37623', 0, 27, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '9:00 AM', 
	'9:50 AM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '444', '01', '92563', 0, 30, '2024-08-23', 'Room2', 'Greensboro Campus', 'TTH', '5:00 PM', 
	'6:15 PM', 0, 5, 0, 5, null, '14269834'),
	('CSC', '444', '02', '29545', 0, 30, '2024-08-23', 'Room1', 'Greensboro Campus', 'MWF', '11:00 AM', 
	'11:50 AM', 0, 5, 0, 5, null, '14269834');


insert into "Registration"."Course_Requisite" (subject, course_number, req_course_subject,
											req_course_number, prerequisite, corequisite)
values 
	('MAT', '222', 'MAT', '111', true, false),
	('MAT', '333', 'MAT', '222', true, false),
	('MAT', '444', 'MAT', '333', true, false),
	('CSC', '222', 'CSC', '111', true, false),
	('CSC', '333', 'CSC', '222', true, false),
	('CSC', '444', 'CSC', '333', true, false),
	('FRE', '222', 'FRE', '111', true, false),
	('FRE', '333', 'FRE', '222', true, false),
	('FRE', '444', 'FRE', '333', true, false),
	('BIO', '222', 'BIO', '111', true, false),
	('BIO', '333', 'BIO', '222', true, false),
	('BIO', '444', 'BIO', '333', true, false),
	('PHY', '222', 'PHY', '111', true, false),
	('PHY', '333', 'PHY', '222', true, false),
	('PHY', '444', 'PHY', '333', true, false),
	('HIS', '222', 'HIS', '111', true, false),
	('HIS', '333', 'HIS', '222', true, false),
	('HIS', '444', 'HIS', '333', true, false),
	('PHI', '222', 'PHI', '111', true, false),
	('PHI', '333', 'PHI', '222', true, false),
	('PHI', '444', 'PHI', '333', true, false);


insert into "Registration"."Major" (major_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Physics'),
	('French'),
	('Philosophy'),
	('History');


insert into "Registration"."Minor" (minor_name)
values 
	('Math'),
	('Computer Science'),
	('Biology'),
	('Physics'),
	('French'),
	('Philosophy'),
	('History');


insert into "Registration"."Student_Major" (student_pin, major_name)
values 
	('98513241', 'Computer Science'),
	('41236346', 'History'),
	('32187189', 'Math'),
	('32107423', 'Physics');


insert into "Registration"."Student_Minor" (student_pin, minor_name)
values 
	('98513241', 'Philosophy'),
	('41236346', 'French');


insert into "Registration"."Major_Courses" (major_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '222'),
	('Computer Science', 'CSC', '333'),
	('Computer Science', 'CSC', '444'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '222'),
	('Math', 'MAT', '333'),
	('Math', 'MAT', '444'),
	('History', 'HIS', '111'),
	('History', 'HIS', '222'),
	('History', 'HIS', '333'),
	('History', 'HIS', '444'),
	('Philosophy', 'PHI', '111'),
	('Philosophy', 'PHI', '222'),
	('Philosophy', 'PHI', '333'),
	('Philosophy', 'PHI', '444'),
	('Biology', 'BIO', '111'),
	('Biology', 'BIO', '222'),
	('Biology', 'BIO', '333'),
	('Biology', 'BIO', '444'),
	('French', 'FRE', '111'),
	('French', 'FRE', '222'),
	('French', 'FRE', '333'),
	('French', 'FRE', '444'),
	('Physics', 'PHY', '111'),
	('Physics', 'PHY', '222'),
	('Physics', 'PHY', '333'),
	('Physics', 'PHY', '444');


insert into "Registration"."Minor_Courses" (minor_name, subject, course_number)
values 
	('Computer Science', 'CSC', '111'),
	('Computer Science', 'CSC', '222'),
	('Math', 'MAT', '111'),
	('Math', 'MAT', '222'),
	('History', 'HIS', '111'),
	('History', 'HIS', '222'),
	('Philosophy', 'PHI', '111'),
	('Philosophy', 'PHI', '222'),
	('Biology', 'BIO', '111'),
	('Biology', 'BIO', '222'),
	('French', 'FRE', '111'),
	('French', 'FRE', '222'),
	('Physics', 'PHY', '111'),
	('Physics', 'PHY', '222');


insert into "Registration"."Student_Courses_Completed" (student_pin, subject, course_number)
values 	
	('98513241', 'CSC', '111'),
	('98513241', 'CSC', '222'),
	('32187189', 'MAT', '111'),
	('32187189', 'MAT', '222'),
	('32107423', 'PHY', '111'),
	('32107423', 'PHY', '222'),
	('32107423', 'PHY', '333');












	
