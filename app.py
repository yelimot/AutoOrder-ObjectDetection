from flask import Flask, request, json, jsonify
import Functions.easy_ocr.text_detection as td

app = Flask(__name__)


@app.route('/analyse', methods=['POST'])
def index():
    f = request.files['image']
    result = td.analyse(f)
    response = app.response_class(response=json.dumps("Error"), status=201, mimetype='application/json')
    
    if(result != "Error"):
        response = app.response_class(response=json.dumps(result), status=200, mimetype='application/json')
   
    return response
    