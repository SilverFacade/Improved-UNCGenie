from flask import Flask, jsonify, request
import psycopg2
import json

app = Flask(__name__)

# just to test connection between frontend and backend
@app.route("/api/schedule")
def schedule():
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


# handles user authentication
@app.route("/api/login", methods=['POST'])
def verifyCredentials():
    pin = request.json.get('username')
    password = request.json.get('password')

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

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    # if the pin and id don't match a record in Person table
    if rv < 1:   
        return {'message':'Wrong PIN or password', 'status' : 401}, 401

    return {'message':'Successfully Logged in', 'status' : 200}, 200

if __name__ == "__main__":
    app.run(debug=True)