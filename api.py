import flask
import dataOperator
from flask import request, jsonify
data = dataOperator.dataOperator()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return data.readJSON()

@app.route('/deleteField', methods=['DELETE'])
def deleteFieldJSON():
    data.deleteFieldJSON(request.json)
    return data.readJSON()

@app.route('/createField', methods=['POST'])
def createField():
    data.addFieldJSON(request.json)
    return data.readJSON()

@app.route('/append', methods=['POST'])
def append():
    data.appendJSON(request.json)
    return data.readJSON()

@app.route('/add', methods=['GET'])
def add():
    field = request.args.get('field')
    value = request.args.get('value')
    return data.changeFieldValue(field,value,"addition")
@app.route('/sub', methods=['GET'])
def sub():
    field = request.args.get('field')
    value = request.args.get('value')
    return data.changeFieldValue(field,value,"subtraction")

app.run()