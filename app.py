#!flask/bin/python
from flask import Flask, jsonify
 
app = Flask(__name__)
 
def calc(arr):
    myArray = []
    for element in arr:
        myArray.append(element*69)
    return myArray
 
@app.route('/calculate/<string:numbers>', methods=['GET'])
def multiply(numbers):
    numbersArray = list(map(int, numbers.split(',')))
    return jsonify(calc(numbersArray))
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)