from flask import Flask, jsonify, request
from flask_cors import CORS
import data_main

app = Flask(__name__)
CORS(app)

@app.route('/raw_data')
def page1():
    print('Incoming...GET...')
    return data_main.get_data() # serialize and use JSON headers

@app.route('/corr')
def corr():

    attr_var = request.args.get('attr_var')
    print('Incoming...GET...Correlation for : '+attr_var)
    return data_main.get_Correlation(attr_var) # serialize and use JSON headers

app.run()