from flask import Flask, jsonify, request
from flask_cors import CORS
import data_main

app = Flask(__name__)
CORS(app)

@app.route('/page1')
def page1():

    # POST request
    if request.method == 'POST':
        print('Incoming...POST...')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    data = data_main.get_data()
    print('Incoming...GET...')
    message = {'greeting': 'Hello from Flask!'}
    return data # serialize and use JSON headers

@app.route('/corr')
def corr():

    # POST request
    if request.method == 'POST':
        print('Incoming...POST...')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    data = data_main.get_Correlation()
    print('Incoming...GET...')
    message = {'greeting': 'Hello from Flask!'}
    return data # serialize and use JSON headers

app.run()