from flask import Flask, jsonify, request
from functools import wraps
from operator import length_hint 
import jwt
import datetime
import psycopg2
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poaynawfcdaferqfdsharh'

# Wrapped and Wrapper function to handle the token that should be received from the client
# to validate their identity
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['token']

        if not token:
            return jsonify({'message' : 'No token given'}), 401

        try:      
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            pin = data['pin']
        except:
            return jsonify({'message' : 'Token is invalid'}), 401

        return f(pin, *args, **kwargs)

    return decorated



# The Login route receives the PIN and password from the client validates them with the database
@app.route("/api/login", methods=['POST'])
def login():
    pin = request.json['username']
    password = request.json['password']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

    try:
        cur = conn.cursor()

        # instructors can't log in for now
        
        script = ''' SELECT COUNT(*)
	                FROM "Registration"."Person"
	                WHERE pin = %s and password = %s '''

        cur.execute(script, (pin, password))

        rv = cur.fetchone()
        rv = int(rv[0])

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    # if the pin and id don't match a record in Person table
    if rv < 1:   
        return jsonify({'message':'Wrong PIN or password', 'status' : '401'}), 401

    # make token 365 days for now
    token = jwt.encode({'pin' : pin, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=365)}, app.config['SECRET_KEY'])

    return jsonify({'token' : token, 'status' : 200}), 200



# The student endpoint returns information about the student in the person table. (maybe from
# Student table and Student_Major and Student_Minor too)
@app.route("/api/student", methods=['GET'])
@token_required
def student(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT *
                    FROM "Registration"."Student" left join "Registration"."Person" on
                    "Registration"."Student".pin = "Registration"."Person".pin  left join 
                    "Registration"."Student_Major" on "Registration"."Student".pin = "Registration"."Student_Major".student_pin
                    left join "Registration"."Student_Minor" on 
                    "Registration"."Student".pin = "Registration"."Student_Minor".student_pin
                    WHERE "Registration"."Student".pin = %s '''
      
        cur.execute(script, (pin,))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The schedule route returns a client's schedule (only 1)
@app.route("/api/schedule", methods=['GET'])
@token_required
def schedule(pin):
    # Get info from client that will be used to query database, pin is passed to all endpoints 
    # from the token validation wrapped function.
    # (commented out the data given from client below since we're only doing 1 schedule, other endpoints
    # receive data like /api/sections endpoint just below this)

    # schedule = request.json['schedule']   / getting rid of multiple schedule for now

    # connects to the database, all endpoints need it. You will need to have the database set up
    # on your computer to connect and query to it (README on github to set it up for windows)
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        # to store database query results
        cur = conn.cursor()

        # The query (check out schemaSQL.sql file in databaseSQL to see database schema)
        # You should probably test the query in dbeaver first 
        script = ''' SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
                    "Registration"."Schedule".section_number, "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active, "Registration"."Section".crn,
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
                    WHERE student_pin = %s '''

        # execute query, adding pin  where %s is in query to prevent sql injection
        # need , after pin despite 1 argument
        cur.execute(script, (pin, ))
           
        # Storing data from query in rv. cur.fetchall fetches all the records returned from query,
        # this adds the keys to the values so we have key-value pairs when returning the json file
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    # close the cursor and connection when done with them
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    # jsonify to get in json format then return the results of query to client.
    # To view the json data go to localhost:5000/api/schedule in browser if running flask server on
    # port 5000, which if using "py app.py" to start it should be (have to remove @token_required
    # at beginning of this route or you will get an error). (200 is just signifying success of api request)
    return jsonify(rv), 200



# The sections endpoint returns the sections the client wants
@app.route("/api/sections", methods=['GET'])
@token_required
def sections(pin):
    subject = request.headers['subject']
    courseNumber = request.headers['courseNumber']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT "Registration"."Section".subject, 
                    "Registration"."Section".course_number, 
                    "Registration"."Section".section_number,
                    "Registration"."Section".days, "Registration"."Section".crn,
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active,
                    "Registration"."Section".waitlist_capacity, "Registration"."Person".last_name,
                    "Registration"."Course".title
                    FROM "Registration"."Section" left join "Registration"."Course" on
                    "Registration"."Section".course_number = "Registration"."Course".course_number and 
                    "Registration"."Section".subject = "Registration"."Course".subject
                    left join "Registration"."Person" on
                    "Registration"."Section".instructor_pin = "Registration"."Person".pin
                    WHERE "Registration"."Section".subject = %s and "Registration"."Section".course_number = %s '''
      
        cur.execute(script, (subject, courseNumber))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The courses endpoint returns the courses and course info the client wants
@app.route("/api/courses", methods=['GET'])
@token_required
def courses(pin):
    subject = request.headers['subject']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT *
                    FROM "Registration"."Course" 
                    WHERE "Registration"."Course".subject = %s '''
      
        cur.execute(script, (subject, ))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The courses_remaining endpoint returns the courses a student has to complete to get their degree
@app.route("/api/courses_remaining", methods=['GET'])
@token_required
def courses_remaining(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        # get major of student first
        script = ''' SELECT major_name
                    FROM "Registration"."Student_Major" 
                    WHERE "Registration"."Student_Major".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        major = rv[0]

        # get minor of student
        script = ''' SELECT minor_name
                    FROM "Registration"."Student_Minor" 
                    WHERE "Registration"."Student_Minor".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        minor = rv[0]

        script = ''' SELECT "Registration"."Major_Courses".subject,
                    "Registration"."Major_Courses".course_number
                    FROM "Registration"."Major_Courses"
                    left join "Registration"."Student_Courses_Completed" on
                    "Registration"."Major_Courses".subject = "Registration"."Student_Courses_Completed".subject and
                    "Registration"."Major_Courses".course_number = "Registration"."Student_Courses_Completed".course_number 
                    WHERE "Registration"."Major_Courses".major_name = %s and 
                    "Registration"."Student_Courses_Completed".subject IS NULL and 
                    "Registration"."Student_Courses_Completed".course_number IS NULL
                    ORDER BY "Registration"."Major_Courses".course_number'''
      
        cur.execute(script, (major, ))       
        
        rv1 = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

        script = ''' SELECT "Registration"."Minor_Courses".subject,
                    "Registration"."Minor_Courses".course_number
                    FROM "Registration"."Minor_Courses"
                    left join "Registration"."Student_Courses_Completed" on
                    "Registration"."Minor_Courses".subject = "Registration"."Student_Courses_Completed".subject and
                    "Registration"."Minor_Courses".course_number = "Registration"."Student_Courses_Completed".course_number 
                    WHERE "Registration"."Minor_Courses".minor_name = %s and 
                    "Registration"."Student_Courses_Completed".subject IS NULL and 
                    "Registration"."Student_Courses_Completed".course_number IS NULL
                    ORDER BY "Registration"."Minor_Courses".course_number'''
      
        cur.execute(script, (minor, ))   

        rv2 = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

        rv = rv1 + rv2

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The courses_completed endpoint returns the courses a student has completed from the 
# Student_Courses_Completed table
@app.route("/api/courses_completed", methods=['GET'])
@token_required
def courses_completed(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT *
                    FROM "Registration"."Student_Courses_Completed" 
                    WHERE "Registration"."Student_Courses_Completed".student_pin = %s '''
      
        cur.execute(script, (pin, ))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The major_courses endpoint returns the courses needed to satisfy a major from the 
# Major_Courses table
@app.route("/api/major_courses", methods=['GET'])
@token_required
def major_courses(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        # get major of student first
        script = ''' SELECT major_name
                    FROM "Registration"."Student_Major" 
                    WHERE "Registration"."Student_Major".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        major = rv[0]

        script = ''' SELECT *
                    FROM "Registration"."Major_Courses" 
                    WHERE "Registration"."Major_Courses".major_name = %s '''
      
        cur.execute(script, (major, ))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200 



# The minor_courses endpoint returns the courses needed to satisfy a minor from the 
# Minor_Courses table
@app.route("/api/minor_courses", methods=['GET'])
@token_required
def minor_courses(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        # get minor of student first
        script = ''' SELECT minor_name
                    FROM "Registration"."Student_Minor" 
                    WHERE "Registration"."Student_Minor".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        minor = rv[0]

        script = ''' SELECT *
                    FROM "Registration"."Minor_Courses" 
                    WHERE "Registration"."Minor_Courses".minor_name = %s '''
      
        cur.execute(script, (minor, ))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200 


# The subjects endpoints selects the subjects in the database
@app.route("/api/subjects", methods=['GET'])
@token_required
def subject(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT DISTINCT subject
                    FROM "Registration"."Course"'''
      
        cur.execute(script)     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200 


# The courseNumbers endpoint selects all the courses of a subject
@app.route("/api/courseNumbers", methods=['GET'])
@token_required
def courseNums(pin):
    subject = request.headers['subject']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT course_number
                    FROM "Registration"."Course"
                    WHERE "Registration"."Course"."subject" = %s '''
      
        cur.execute(script, (subject, ))     
        
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200 


# The graduation_progress endpoint calculates the progress toward graduation and return it.
@app.route("/api/graduation_progress", methods=['GET'])
@token_required
def graduation_progress(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        # get major of student first
        script = ''' SELECT major_name
                    FROM "Registration"."Student_Major" 
                    WHERE "Registration"."Student_Major".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        major = rv[0]

        # get minor of student
        script = ''' SELECT minor_name
                    FROM "Registration"."Student_Minor" 
                    WHERE "Registration"."Student_Minor".student_pin =  %s '''
      
        cur.execute(script, (pin, ))     

        rv = cur.fetchone()

        minor = rv[0]

        script = ''' SELECT "Registration"."Major_Courses".subject,
                    "Registration"."Major_Courses".course_number
                    FROM "Registration"."Major_Courses"
                    left join "Registration"."Student_Courses_Completed" on
                    "Registration"."Major_Courses".subject = "Registration"."Student_Courses_Completed".subject and
                    "Registration"."Major_Courses".course_number = "Registration"."Student_Courses_Completed".course_number 
                    WHERE "Registration"."Major_Courses".major_name = %s and 
                    "Registration"."Student_Courses_Completed".subject IS NULL and 
                    "Registration"."Student_Courses_Completed".course_number IS NULL
                    ORDER BY "Registration"."Major_Courses".course_number'''
      
        cur.execute(script, (major, ))       
        
        rv1 = cur.fetchall()

        script = ''' SELECT "Registration"."Minor_Courses".subject,
                    "Registration"."Minor_Courses".course_number
                    FROM "Registration"."Minor_Courses"
                    left join "Registration"."Student_Courses_Completed" on
                    "Registration"."Minor_Courses".subject = "Registration"."Student_Courses_Completed".subject and
                    "Registration"."Minor_Courses".course_number = "Registration"."Student_Courses_Completed".course_number 
                    WHERE "Registration"."Minor_Courses".minor_name = %s and 
                    "Registration"."Student_Courses_Completed".subject IS NULL and 
                    "Registration"."Student_Courses_Completed".course_number IS NULL
                    ORDER BY "Registration"."Minor_Courses".course_number'''
      
        cur.execute(script, (minor, ))   

        rv2 = cur.fetchall()

        courses_remaining = rv1 + rv2

        script = ''' SELECT *
                    FROM "Registration"."Student_Courses_Completed" 
                    WHERE "Registration"."Student_Courses_Completed".student_pin = %s '''
      
        cur.execute(script, (pin, ))   

        courses_completed = cur.fetchall()

        degree_progress = round((len(courses_completed) / (len(courses_completed) + len(courses_remaining))), 3)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify({'progress' : degree_progress}), 200



# The sections_registered endpoint returns the sections a student is registered for from
# the Student_Sections_Registered table 
@app.route("/api/sectionsRegistered", methods=['GET'])
@token_required
def sections_registered(pin):
    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
                    
    try:
        cur = conn.cursor()

        script = ''' SELECT "Registration"."Student_Sections_Registered".subject, 
                    "Registration"."Student_Sections_Registered".course_number, 
                    "Registration"."Student_Sections_Registered".section_number,
                    "Registration"."Section".days, "Registration"."Section".crn,
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active,
                    "Registration"."Section".waitlist_capacity, "Registration"."Person".last_name,
                    "Registration"."Course".title
                    FROM "Registration"."Student_Sections_Registered" inner join "Registration"."Section" on 
                    "Registration"."Section".course_number = "Registration"."Student_Sections_Registered".course_number and 
                    "Registration"."Section".section_number = "Registration"."Student_Sections_Registered".section_number and 
                    "Registration"."Section".subject = "Registration"."Student_Sections_Registered".subject
                    left join "Registration"."Course" on
                    "Registration"."Section".course_number = "Registration"."Course".course_number and 
                    "Registration"."Section".subject = "Registration"."Course".subject
                    left join "Registration"."Person" on
                    "Registration"."Section".instructor_pin = "Registration"."Person".pin
                    WHERE student_pin = %s '''
      
        cur.execute(script, (pin,))
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The register endpoint registers a student for a section (see if section is full, if not
# move to Student_Sections_Registered table, check prereqs, etc)
@app.route("/api/register", methods=['POST'])
@token_required
def register(pin):
    subject = request.json['subject']
    courseNumber = request.json['courseNumber']
    sectionNumber = request.json['sectionNumber']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

    try:
        cur = conn.cursor()




        # check if already registered
        script = ''' SELECT COUNT(*)
                    FROM "Registration"."Student_Sections_Registered"
                    WHERE student_pin = %s and subject = %s and course_number = %s '''
      
        cur.execute(script, (pin, subject, courseNumber))

        rv = cur.fetchone()
        rv = int(rv[0])

        if rv > 0:
            return jsonify({'status' : '400', 'error' : 'Error: You already registered for this course'}), 400
        



        # check capacity
        script = ''' SELECT active, capacity
                    FROM  "Registration"."Section"
                    WHERE subject = %s and course_number = %s and section_number = %s '''
      
        cur.execute(script, (subject, courseNumber, sectionNumber))



        rv = cur.fetchone()
        active = rv[0]
        capacity = rv[1]

        if active >= capacity:
            return jsonify({'status' : '400', 'error' : 'Error: Full Capacity'}), 400




        # check if student meets requisites
        script = ''' SELECT req_course_subject, req_course_number
                    FROM  "Registration"."Course_Requisite"
                    WHERE subject = %s and course_number = %s '''
      
        cur.execute(script, (subject, courseNumber))

        rv = cur.fetchall()

        print(rv)
        
        requisites = rv

        if rv:
            listLength = length_hint(requisites)
            number = 0

            while number < listLength:
                # if the required course is in the student_courses_completed table that means the student completed it
                script = ''' select count(*)
                            from "Registration"."Student_Courses_Completed"
                            where "Registration"."Student_Courses_Completed".subject = %s 
                            and "Registration"."Student_Courses_Completed".course_number = %s
                            and "Registration"."Student_Courses_Completed".student_pin = %s '''
      
                cur.execute(script, (requisites[number][0], requisites[number][1], pin))

                rv = cur.fetchall()

                print(rv[0][0])

                number += 1

                # if student hasn't completed the requisite course
                if rv[0][0] == 0:
                    return jsonify({'status' : '400', 'error' : 'Error: Requisites not met'}), 400




        # check for time overlap/conflicts
        # only checks for exact start and end time overlaps
        script = ''' SELECT start_time, end_time, days
                    FROM "Registration"."Section"
                    WHERE  subject = %s and course_number = %s and section_number = %s'''
      
        cur.execute(script, (subject, courseNumber, sectionNumber))

        section_time = cur.fetchone()
        
        start_time = section_time[0]
        end_time = section_time[1]
        days = section_time[2]

        script = ''' SELECT count(*)
                    FROM "Registration"."Student_Sections_Registered" inner join "Registration"."Section" on
                    "Registration"."Section".course_number = "Registration"."Student_Sections_Registered".course_number and 
                    "Registration"."Section".section_number = "Registration"."Student_Sections_Registered".section_number and 
                    "Registration"."Section".subject = "Registration"."Student_Sections_Registered".subject
                    WHERE  start_time = %s and end_time = %s and days = %s'''

        cur.execute(script, (start_time, end_time, days))

        rv = cur.fetchone()

        rv = int(rv[0])

        if rv > 0:
            return jsonify({'status' : '400', 'error' : 'Error: Time Conflict'}), 400






        script = ''' INSERT INTO "Registration"."Student_Sections_Registered" (student_pin, subject, course_number,
                    section_number)
                    VALUES (%s, %s, %s, %s) '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()
    
        # increment capacity by 1 for section
        script = ''' UPDATE "Registration"."Section"
                    SET active = active + 1
                    WHERE subject = %s and course_number = %s and section_number = %s  '''
      
        cur.execute(script, (subject, courseNumber, sectionNumber))

        conn.commit()

        # same script as sections_registered route
        script = ''' SELECT "Registration"."Student_Sections_Registered".subject, 
                    "Registration"."Student_Sections_Registered".course_number, 
                    "Registration"."Student_Sections_Registered".section_number,
                    "Registration"."Section".days, "Registration"."Section".crn,
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active,
                    "Registration"."Section".waitlist_capacity, "Registration"."Person".last_name,
                    "Registration"."Course".title
                    FROM "Registration"."Student_Sections_Registered" inner join "Registration"."Section" on 
                    "Registration"."Section".course_number = "Registration"."Student_Sections_Registered".course_number and 
                    "Registration"."Section".section_number = "Registration"."Student_Sections_Registered".section_number and 
                    "Registration"."Section".subject = "Registration"."Student_Sections_Registered".subject
                    left join "Registration"."Course" on
                    "Registration"."Section".course_number = "Registration"."Course".course_number and 
                    "Registration"."Section".subject = "Registration"."Course".subject
                    left join "Registration"."Person" on
                    "Registration"."Section".instructor_pin = "Registration"."Person".pin
                    WHERE student_pin = %s '''
      
        cur.execute(script, (pin,))
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The add_to_Schedule endpoint adds a section to a student's schedule (check time conflicts)
@app.route("/api/addToSchedule", methods=['POST'])
@token_required
def add_to_Schedule(pin):
    subject = request.json['subject']
    courseNumber = request.json['courseNumber']
    sectionNumber = request.json['sectionNumber']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

    try:
        cur = conn.cursor()

        # check if already in schedule
        script = ''' SELECT COUNT(*)
                    FROM "Registration"."Schedule" 
                    WHERE student_pin = %s and subject = %s and course_number = %s and section_number = %s '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        rv = cur.fetchone()
        rv = int(rv[0])

        if rv > 0:
            return jsonify({'status' : '400', 'error' : 'Error: Already in Schedule'}), 400
            
        # check for requisites satisfied    
        script = ''' SELECT req_course_subject, req_course_number
                    FROM  "Registration"."Course_Requisite"
                    WHERE subject = %s and course_number = %s '''
      
        cur.execute(script, (subject, courseNumber))

        rv = cur.fetchall()

        if rv:
            listLength = length_hint(rv)
            number = 0

            while number < listLength:
                script = ''' select count(*)
                            from "Registration"."Course_Requisite" inner join "Registration"."Student_Courses_Completed" on
                            "Registration"."Student_Courses_Completed".subject = "Registration"."Course_Requisite".req_course_subject
                            and "Registration"."Student_Courses_Completed".course_number = "Registration"."Course_Requisite".req_course_number
                            where "Registration"."Course_Requisite".req_course_subject = %s 
                            and "Registration"."Course_Requisite".req_course_number = %s
                            and "Registration"."Student_Courses_Completed".student_pin = %s '''
      
                cur.execute(script, (rv[number][0], rv[number][1], pin))

                rv = cur.fetchone()

                rv = int(rv[0])

                number += 1

                # if student hasn't met requisites
                if rv < 1:
                    return jsonify({'status' : '400', 'error' : 'Error: Requisites not met'}), 400

        script = ''' INSERT INTO "Registration"."Schedule" (student_pin, schedule_name, subject, course_number,
                    section_number)
                    VALUES (%s, 'defaultScheName', %s, %s, %s)  '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        script = ''' SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
                    "Registration"."Schedule".section_number, "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active, "Registration"."Section".crn,
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
                    WHERE student_pin = %s '''
      
        cur.execute(script, (pin,))
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The drop endpoint drops a section from the registered sections table
@app.route("/api/dropSection", methods=['POST'])
@token_required
def drop(pin):
    subject = request.json['subject']
    courseNumber = request.json['courseNumber']
    sectionNumber = request.json['sectionNumber']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

    try:
        cur = conn.cursor()

        script = ''' DELETE FROM "Registration"."Student_Sections_Registered"
                    WHERE student_pin = %s and subject = %s and 
                    course_number = %s and section_number = %s '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        script = ''' UPDATE "Registration"."Section"
                    SET active = active - 1
                    WHERE subject = %s and course_number = %s and section_number = %s  '''
      
        cur.execute(script, (subject, courseNumber, sectionNumber))

        conn.commit()

        script = ''' SELECT "Registration"."Student_Sections_Registered".subject, 
                    "Registration"."Student_Sections_Registered".course_number, 
                    "Registration"."Student_Sections_Registered".section_number,
                    "Registration"."Section".days, "Registration"."Section".crn,
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active,
                    "Registration"."Section".waitlist_capacity, "Registration"."Person".last_name,
                    "Registration"."Course".title
                    FROM "Registration"."Student_Sections_Registered" inner join "Registration"."Section" on 
                    "Registration"."Section".course_number = "Registration"."Student_Sections_Registered".course_number and 
                    "Registration"."Section".section_number = "Registration"."Student_Sections_Registered".section_number and 
                    "Registration"."Section".subject = "Registration"."Student_Sections_Registered".subject
                    left join "Registration"."Course" on
                    "Registration"."Section".course_number = "Registration"."Course".course_number and 
                    "Registration"."Section".subject = "Registration"."Course".subject
                    left join "Registration"."Person" on
                    "Registration"."Section".instructor_pin = "Registration"."Person".pin
                    WHERE student_pin = %s '''
      
        cur.execute(script, (pin,))
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



# The remove_from_Schedule endpoint removes a section from a student's schedule
@app.route("/api/removeFromSchedule", methods=['POST'])
@token_required
def remove_from_Schedule(pin):
    subject = request.json['subject']
    courseNumber = request.json['courseNumber']
    sectionNumber = request.json['sectionNumber']

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)

    try:
        cur = conn.cursor()

        script = ''' DELETE FROM "Registration"."Schedule"
                    WHERE student_pin = %s and subject = %s and 
                    course_number = %s and section_number = %s '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        script = ''' SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
                    "Registration"."Schedule".section_number, "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".start_time, "Registration"."Section".end_time,
                    "Registration"."Section".waitlist_active, "Registration"."Section".crn,
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
                    WHERE student_pin = %s '''
      
        cur.execute(script, (pin,))
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return jsonify(rv), 200



if __name__ == "__main__":
    app.run(debug=True)
