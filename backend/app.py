from flask import Flask, jsonify, request
from functools import wraps
import jwt
import datetime
import psycopg2
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poaynawfcdaferqfdsharh'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args['token']

        if not token:
            return jsonify({'message' : 'No token given'}), 401

        try:      
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message' : 'Token is invalid'}), 401

        #pass current PIN?
        return f(*args, **kwargs)

    return decorated

# TODO: add tokens to database
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
        return jsonify({'message':'Wrong PIN or password', 'status' : '401'}), 401

    token = jwt.encode({'pin' : pin, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=10)}, app.config['SECRET_KEY'])

    return jsonify({'token' : token, 'status' : 200}), 200




# TODO: logout (make blocklist for tokens?)
@app.route("/api/logout", methods=['GET'])
def logout():
    return


# just to test connection between frontend and backend
@app.route("/api/schedule", methods=['GET'])
@token_required
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


if __name__ == "__main__":
    app.run(debug=True)