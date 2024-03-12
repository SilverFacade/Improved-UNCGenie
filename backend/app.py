from flask import Flask, jsonify, request, session
import psycopg2
import json

app = Flask(__name__)
app.secret_key = "1095b7236v4c5-08Aert915v1dy345wdSGFD"

# login
@app.route("/api/login", methods=['POST', 'GET'])
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
	                WHERE pin = '{}' and password = '{}' '''.format(pin, password)

        cur.execute(script)

        rv = cur.fetchone()
        rv = int(rv[0])

        session["user_pin"] = pin

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    # if the pin and id don't match a record in Person table
    if rv < 1:   
        return {'message':'Wrong PIN or password', 'status' : '401'}, 401

    return {'message':'Successfully Logged in', 'status' : '200'}, 200




# logout
@app.route("/api/logout", methods=['GET'])
def logout():
    session.pop("user_pin", None)
    return 




# just to test connection between frontend and backend
@app.route("/api/schedule")
def schedule():
    #verify session for user, redirect to login page if invalid.
    if "user_pin" in session:
        pin = session["user_pin"]

    conn = psycopg2.connect(host = 'localhost',
                        dbname = 'webregistrationapp',
                        user = 'postgres',
                        password = '1234',
                        port = 5432)
    try:
        cur = conn.cursor()

        script = ''' SELECT subject, course_number, section_number
                    FROM "Registration"."Schedule"
                    WHERE student_pin = '98513241' and schedule_name = 'Rosie Schedule' '''

        cur.execute(script)
           
        rv = [dict((cur.description[i][0], value)  \
            for i, value in enumerate(row)) for row in cur.fetchall()]

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return rv


if __name__ == "__main__":
    app.run(debug=True)