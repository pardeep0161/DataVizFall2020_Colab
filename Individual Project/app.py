from flask import Flask, jsonify, request
from flask_cors import CORS
import data_main

app = Flask(__name__)
CORS(app)

@app.route('/bar')
def bar():
    print('Incoming...GET...')
    return data_main.get_latest_data() # serialize and use JSON headers

@app.route('/raw_data')
def page1():
    print('Incoming...GET...')
    return data_main.get_data() # serialize and use JSON headers

@app.route('/corr')
def corr():
    corr_attr = request.args.get('corr_attr')
    year = request.args.get('year')
    print('Incoming...GET...Correlation for : '+corr_attr+' '+year)
    return data_main.get_Correlation(corr_attr, year) # serialize and use JSON headers

app.run()