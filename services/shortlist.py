from flask import Flask, jsonify, make_response
import requests
import os
import json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/database/companies.json".format(database_path), "r") as f:
    company = json.load(f)

with open("{}/database/users.json".format(database_path), "r") as u:
    usr = json.load(u)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hello"

@app.route('/companies', methods=['GET'])
def companies():
    ''' Returns the list of companies '''

    resp = make_response(json.dumps(company, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/companies/<company_name>', methods=['GET'])
def shortlist_data(company_name):
    ''' Returns info about a shortlisted students '''

    # if username not in usr:
    #     return "Not found"

    result = []

    pointer = company[company_name]["criteria"]

    for user in usr:
        user_pointer = usr[user]["pointer"]
        if user_pointer >= pointer:
            result.append(usr[user])

    return jsonify(lists=result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)