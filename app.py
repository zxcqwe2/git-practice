from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Python Calculator API!"

@app.route('/add/<float:a>/<float:b>')
def add(a, b):
    return {'result': a + b}

@app.route('/subtract/<float:a>/<float:b>')
def subtract(a, b):
    return {'result': a - b}

@app.route('/multiply/<float:a>/<float:b>')
def multiply(a, b):
    return {'result': a * b}

@app.route('/divide/<float:a>/<float:b>')
def divide(a, b):
    if b == 0:
        return {'error': 'Cannot divide by zero'}, 400
    return {'result': a / b}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)