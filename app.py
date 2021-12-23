from flask import Flask, request, json, jsonify
import Functions.easy_ocr.text_detection as td

app = Flask(__name__)


@app.route('/analyse', methods=['GET'])
def index():
    result = td.analyse()
    response = app.response_class(response=json.dumps("Error"), status=201, mimetype='application/json')
    
    if(result != "Error"):
        response = app.response_class(response=json.dumps(result), status=200, mimetype='application/json')
   
    return response
    
