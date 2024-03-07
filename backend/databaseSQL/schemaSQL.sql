CREATE SCHEMA "Registration";

/*
 * Table for data about all users of the App
 */
CREATE TABLE "Registration"."Person" (
  "pin" char(8) PRIMARY KEY,
  "first_name" varchar(30) NOT NULL,
  "last_name" varchar(30) NOT NULL,
  "password" char(6) NOT NULL,
  "address" varchar(50),
  "email" varchar(30) NOT NULL,
  "phone_number" varchar(15)
);

/*
 * Table for students
 */
CREATE TABLE "Registration"."Student" (
  "pin" char(8) PRIMARY KEY,
  "year" varchar(10) NOT NULL,
  "emergency_contact" varchar(15)
);

/*
 * Table for instructors
 */
CREATE TABLE "Registration"."Instructor" (
  "pin" char(8) PRIMARY KEY,
  "department" varchar(30) NOT NULL
);

/*
 * Table that holds the sections on a student's schedule (a student can have many schedules)
 */
CREATE TABLE "Registration"."Schedule" (
  "student_pin" char(8),
  "schedule_name" varchar(30),
  "subject" char(3),
  "course_number" char(3),
  "section_number" char(2),
  PRIMARY KEY ("student_pin", "schedule_name", "subject", "course_number", "section_number")
);

/*
 * Table to that holds all the majors offered at the University
 */
CREATE TABLE "Registration"."Major" (
  "major_name" varchar(30) PRIMARY KEY
);

/*
 * Table that holds all the minors offered at the University (Student must have Major for minor?)
 */
CREATE TABLE "Registration"."Minor" (
  "minor_name" varchar(30) PRIMARY KEY
);

/*
 * Table that holds all the Courses that are offered
 */
CREATE TABLE "Registration"."Course" (
  "subject" char(3),
  "course_number" char(3),
  "title" varchar(40),
  "credits" int NOT NULL,
  "requisites" bool,
  PRIMARY KEY ("subject", "course_number")
);

/*
 * Table that holds all the sections that can be registered for by students
 */
CREATE TABLE "Registration"."Section" (
  "subject" char(3),
  "course_number" char(3),
  "section_number" char(2),
  "crn" char(5) NOT NULL,
  "capacity" int NOT NULL,
  "start_date" date,
  "location" varchar(50),
  "campus" varchar(50),
  "days" varchar(10),
  "waitlist_active" int,
  "waitlist_capacity" int,
  "xl_active" int,
  "xl_capacity" int,
  "attribute" varchar(100),
  "instructor_pin" char(8),
  PRIMARY KEY ("subject", "course_number", "section_number")
);

/*
 * Table that holds the prerequisites and coquisites for courses
 */
CREATE TABLE "Registration"."Course_Requisite" (
  "subject" char(3),
  "course_number" char(3),
  "req_course_subject" char(3),
  "req_course_number" char(3),
  "prerequisite" bool,
  "corequisite" bool,
  PRIMARY KEY ("subject", "course_number", "req_course_subject", "req_course_number")
);

/*
 * Table that holds each Major a Student is enrolled in
 */
CREATE TABLE "Registration"."Student_Major" (
  "student_pin" char(8),
  "major_name" varchar(30),
  PRIMARY KEY ("student_pin", "major_name")
);

/*
 * Table that holds each Minor a Student is enrolled in
 */
CREATE TABLE "Registration"."Student_Minor" (
  "student_pin" char(8),
  "minor_name" varchar(30),
  PRIMARY KEY ("student_pin", "minor_name")
);

/*
 * Table that holds the courses required to finish a major
 */
CREATE TABLE "Registration"."Major_Courses" (
  "major_name" varchar(30),
  "subject" char(3),
  "course_number" char(3),
  PRIMARY KEY ("major_name", "subject", "course_number")
);

/*
 * Table that holds the courses required to finish a minor
 */
CREATE TABLE "Registration"."Minor_Courses" (
  "minor_name" varchar(30),
  "subject" char(3),
  "course_number" char(3),
  PRIMARY KEY ("minor_name", "subject", "course_number")
);

/*
 * Table that lists the sections that a student is enrolled in
 */
CREATE TABLE "Registration"."Student_Sections_Enrolled" (
  "student_pin" char(8),
  "subject" char(3),
  "course_number" char(3),
  "section_number" char(2),
  PRIMARY KEY ("student_pin", "subject", "course_number", "section_number")
);

/*
 * Table that lists the students completed courses
 */
CREATE TABLE "Registration"."Student_Courses_Completed" (
  "student_pin" char(8),
  "subject" char(3),
  "course_number" char(3),
  "grade" varchar(3),
  PRIMARY KEY ("student_pin", "subject", "course_number")
);

ALTER TABLE "Registration"."Student" ADD FOREIGN KEY ("pin") REFERENCES "Registration"."Person" ("pin");

ALTER TABLE "Registration"."Instructor" ADD FOREIGN KEY ("pin") REFERENCES "Registration"."Person" ("pin");

ALTER TABLE "Registration"."Section" ADD FOREIGN KEY ("instructor_pin") REFERENCES "Registration"."Instructor" ("pin");

ALTER TABLE "Registration"."Section" ADD FOREIGN KEY ("subject", "course_number") REFERENCES "Registration"."Course" ("subject", "course_number");

ALTER TABLE "Registration"."Schedule" ADD FOREIGN KEY ("subject", "course_number", "section_number") REFERENCES "Registration"."Section" ("subject", "course_number", "section_number");

ALTER TABLE "Registration"."Course_Requisite" ADD FOREIGN KEY ("subject", "course_number") REFERENCES "Registration"."Course" ("subject", "course_number");

ALTER TABLE "Registration"."Student_Major" ADD FOREIGN KEY ("student_pin") REFERENCES "Registration"."Student" ("pin");

ALTER TABLE "Registration"."Student_Major" ADD FOREIGN KEY ("major_name") REFERENCES "Registration"."Major" ("major_name");

ALTER TABLE "Registration"."Student_Minor" ADD FOREIGN KEY ("student_pin") REFERENCES "Registration"."Student" ("pin");

ALTER TABLE "Registration"."Student_Minor" ADD FOREIGN KEY ("minor_name") REFERENCES "Registration"."Minor" ("minor_name");

ALTER TABLE "Registration"."Major_Courses" ADD FOREIGN KEY ("major_name") REFERENCES "Registration"."Major" ("major_name");

ALTER TABLE "Registration"."Major_Courses" ADD FOREIGN KEY ("subject", "course_number") REFERENCES "Registration"."Course" ("subject", "course_number");

ALTER TABLE "Registration"."Minor_Courses" ADD FOREIGN KEY ("minor_name") REFERENCES "Registration"."Minor" ("minor_name");

ALTER TABLE "Registration"."Minor_Courses" ADD FOREIGN KEY ("subject", "course_number") REFERENCES "Registration"."Course" ("subject", "course_number");

ALTER TABLE "Registration"."Student_Sections_Enrolled" ADD FOREIGN KEY ("student_pin") REFERENCES "Registration"."Student" ("pin");

ALTER TABLE "Registration"."Student_Sections_Enrolled" ADD FOREIGN KEY ("subject", "course_number", "section_number") REFERENCES "Registration"."Section" ("subject", "course_number", "section_number");

ALTER TABLE "Registration"."Student_Courses_Completed" ADD FOREIGN KEY ("student_pin") REFERENCES "Registration"."Student" ("pin");

ALTER TABLE "Registration"."Student_Courses_Completed" ADD FOREIGN KEY ("subject", "course_number") REFERENCES "Registration"."Course" ("subject", "course_number");

