from flask import Flask, request, json, jsonify
import Functions.easy_ocr.text_detection as td

app = Flask(__name__)


@app.route('/analyse', methods=['POST'])
def index():
    config = request.form.get("config")
    f = request.files['image']
    result = td.analyse(f,config)
    response = app.response_class(response=json.dumps(result), status=201, mimetype='application/json')
    
    if(isinstance(result,list)):
        response = app.response_class(response=json.dumps(result), status=200, mimetype='application/json')
   
    return response
    