from flask import Flask, jsonify, request
from functools import wraps
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

        #token allows passing of current user's pin to the endpoints
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

    token = jwt.encode({'pin' : pin, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=10)}, app.config['SECRET_KEY'])

    return jsonify({'token' : token, 'status' : 200}), 200



# The schedule route receives a schedule name from the client (specific to user) and returns
# the data in the data in the Schedule table that matches that student's schedule name
@app.route("/api/schedule", methods=['GET'])
@token_required
def schedule(pin):
    # Get info from client that will be used to query database, pin is passed to all endpoints 
    # from the token validation wrapped function.

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
                    WHERE student_pin = %s '''

        # execute query, adding pin  where %s is in query to prevent sql injection
        # need , after pin despite 1 argument
        cur.execute(script, (pin, ))
           
        # Storing data from query in rv. cur.fetchall fetches all the records returned from query,
        # the rest adds the keys to the values so we have key-value pairs when returning the json file
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



#  The sections endpoint returns the sections the client wants
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
                    "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".time,"Registration"."Section".waitlist_active,
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



# TODO: The student endpoint returns information about the student in the person table. (maybe from
# Student table and Student_Major and Student_Minor too)
@app.route("/api/student", methods=['GET'])
@token_required
def student(pin):
    return 



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
                    "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".time,"Registration"."Section".waitlist_active,
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
        # TODO: check for requisites first
        # TODO: check if already exists in Student_Sections_Registered table
        # TODO: check for time overlap/conflicts

        cur = conn.cursor()

        script = ''' INSERT INTO "Registration"."Student_Sections_Registered" (student_pin, subject, course_number,
                    section_number)
                    VALUES (%s, %s, %s, %s) '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        #remove from schedule table if it was in there
        script = ''' DELETE FROM "Registration"."Schedule"
                    WHERE student_pin = %s and subject = %s and 
                    course_number = %s and section_number = %s '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        # same script as sections_registered route
        script = ''' SELECT "Registration"."Student_Sections_Registered".subject, 
                    "Registration"."Student_Sections_Registered".course_number, 
                    "Registration"."Student_Sections_Registered".section_number,
                    "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".time,"Registration"."Section".waitlist_active,
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

        script = ''' SELECT "Registration"."Student_Sections_Registered".subject, 
                    "Registration"."Student_Sections_Registered".course_number, 
                    "Registration"."Student_Sections_Registered".section_number,
                    "Registration"."Section".days, 
                    "Registration"."Section".active, "Registration"."Section".capacity,
                    "Registration"."Section".time,"Registration"."Section".waitlist_active,
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



# TODO: The remove_from_Schedule endpoint removes a section from a student's schedule
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



# TODO: The add_to_Schedule endpoint adds a section to a student's schedule (check time conflicts)
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

        script = ''' INSERT INTO "Registration"."Schedule" (student_pin, schedule_name, subject, course_number,
                    section_number)
                    VALUES (%s, 'defaultScheName', %s, %s, %s)  '''
      
        cur.execute(script, (pin, subject, courseNumber, sectionNumber))

        conn.commit()

        script = ''' SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
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



# TODO: The courses endpoint returns the courses the client wants
@app.route("/api/courses", methods=['GET'])
@token_required
def courses(pin):
    return 



# TODO: The courses_completed endpoint returns the courses a student has completed from the 
# Student_Courses_Completed table
@app.route("/api/courses_completed", methods=['GET'])
@token_required
def courses_completed(pin):
    return 



# TODO: The major_courses endpoint returns the courses needed to satisfy a major from the 
# Major_Courses table
@app.route("/api/major_courses", methods=['GET'])
@token_required
def major(pin):
    return 



# TODO: The minor_courses endpoint returns the courses needed to satisfy a minor from the 
# Minor_Courses table
@app.route("/api/minor_courses", methods=['GET'])
@token_required
def minor_courses(pin):
    return 



# TODO: The graduation_progress endpoint calculates the progress toward graduation and return it.
@app.route("/api/graduation_progress", methods=['GET'])
@token_required
def graduation_progress(pin):
    return 



if __name__ == "__main__":
    app.run(debug=True)