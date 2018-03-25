from flask import Flask, jsonify, make_response
import requests
import os
import json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/database/users.json".format(database_path), "r") as f:
    usr = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hello"

@app.route('/users', methods=['GET'])
def users():
    ''' Returns the list of users '''

    resp = make_response(json.dumps(usr, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/users/<username>', methods=['GET', 'POST'])
def user_data(username):
    ''' Returns info about a specific user '''

    if username not in usr:
        new_user = {}
        new_user["id"] = 6
        new_user["name"] = username
        new_user["pointer"] = 7.0
        usr.update(new_user)

        with open('users.json', 'w') as f:
            json.dump(usr, f)
        return "Not found. Added to DB."

    return jsonify(usr[username])

@app.route('/users/<username>/edit', methods=['PUT', 'GET'])
def user_data(username):
    ''' 
    Method not implemented yet.
    Edit user details. Pointer, ID, etc.

    '''

if __name__ == '__main__':
    app.run(port=5000, debug=True)