/*
 * Drops Schema and tables. The order of the drops is important to avoid triggering foreign
 * key constraints
 */

drop table "Registration"."Student_Courses_Completed" ;

drop table "Registration"."Student_Sections_Registered" ;

drop table "Registration"."Minor_Courses" ;

drop table "Registration"."Major_Courses" ;

drop table "Registration"."Student_Minor" ;

drop table "Registration"."Student_Major" ;

drop table "Registration"."Minor";

drop table "Registration"."Major";

drop table "Registration"."Schedule";

drop table "Registration"."Course_Requisite";

drop table "Registration"."Section";

drop table "Registration"."Course";

drop table "Registration"."Instructor";

drop table "Registration"."Student";

drop table "Registration"."Person";

drop schema "Registration";