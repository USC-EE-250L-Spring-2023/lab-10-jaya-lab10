from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/receive1', methods = 'POST')
def receive1():
    data = request.json
    data1 = process1(data)
    return jsonify(data1)

@app.route('/receive2', methods = 'POST')
def receive2():
    data = request.json
    data2 = process2(data)
    return jsonify(data2)

if _name_ == "_main_":
    app.run(host = '0.0.0.0')
