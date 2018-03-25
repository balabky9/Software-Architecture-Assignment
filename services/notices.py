from flask import Flask, jsonify, make_response
import requests
import os
import json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/database/schedule.json".format(database_path), "r") as f:
    sched = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hello"

@app.route('/sched', methods=['GET'])
def schedule():
    ''' Returns the entire schedule '''

    resp = make_response(json.dumps(sched, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/sched/<date>', methods=['GET'])
def date_schedule(date):
    ''' Returns info about a specific user '''

    return jsonify(sched[date])

@app.route('/sched/<date>/edit', methods=['PUT', 'GET'])
def edit_schedule(username):
    ''' 
    Method not implemented yet.
    Edit user details. Pointer, ID, etc.

    '''

if __name__ == '__main__':
    app.run(port=5000, debug=True)