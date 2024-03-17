from flask import Flask, jsonify, request
from functools import wraps
import jwt
import datetime
import psycopg2
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poaynawfcdaferqfdsharh'

# TODO: updates methods allowed for each endpoint

# Wrapped and Wrapper function to handle the token that should be received from the client
# to validate their identity
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.json['token']

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
    schedule = request.json['schedule']

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

        # TODO: add times to Section table?
        # The query (check out schemaSQL.sql file in databaseSQL to see database schema)
        # You should probably test the query in dbeaver first 
        script = ''' SELECT "Registration"."Schedule".subject, "Registration"."Schedule".course_number, 
                    "Registration"."Schedule".section_number, "Registration"."Section".days
                    FROM "Registration"."Schedule" inner join "Registration"."Section" on 
                    "Registration"."Section".course_number = "Registration"."Schedule".course_number and 
                    "Registration"."Section".section_number = "Registration"."Schedule".section_number and 
                    "Registration"."Section".subject = "Registration"."Schedule".subject
                    WHERE student_pin = %s and schedule_name = %s '''

        # execute query, adding pin and schedule where %s is in query (need to be in order) to prevent sql injection
        # is only 1 %s you will still need a comma after it so (pin,)
        cur.execute(script, (pin, schedule))
           
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



# TODO: The student endpoint returns information about the student in the person table. (maybe from
# Student table and Student_Major and Student_Minor too)
@app.route("/api/student", methods=['GET'])
@token_required
def student(pin):
    return 



# TODO: The graduation_progress endpoint calculates the progress toward graduation and return it.
@app.route("/api/graduation_progress", methods=['GET'])
@token_required
def graduation_progress(pin):
    return 



# TODO: The sections_registered endpoint returns the sections a student is registered for from
# the Student_Sections_Enrolled table (may rename table to Student_Sections_Registered)
@app.route("/api/sections_registered", methods=['GET'])
@token_required
def sections_registered(pin):
    return 



# TODO: The register endpoint registers a student for a section (see if section is full, if not
# move to Student_Sections_Enrolled table, check prereqs, etc)
@app.route("/api/register", methods=['GET', 'POST'])
@token_required
def register(pin):
    return 



# TODO: The drop endpoint drops a section from the registered sections table
@app.route("/api/drop", methods=['GET', 'POST'])
@token_required
def drop(pin):
    return 



# TODO: The add_to_Schedule endpoint adds a section to a student's schedule (check time conflicts)
@app.route("/api/add_to_Schedule", methods=['GET', 'POST'])
@token_required
def add_to_Schedule(pin):
    return 



# TODO: The register_Schedule endpoint registers for all the sections in a student's schedule
@app.route("/api/register_Schedule", methods=['GET', 'POST'])
@token_required
def register_Schedule(pin):
    return 



# TODO: The sections endpoint returns the sections the client wants
@app.route("/api/sections", methods=['GET'])
@token_required
def sections(pin):
    return 



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



if __name__ == "__main__":
    app.run(debug=True)