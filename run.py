from os import name
from flask import Flask # from flask module import Flask class


app = Flask(__name__) # notes which part of the flask module we are working in


@app.route('/') 
def index():
    return 'Hello World!'


@app.route('/test') 
def test():
    return 'test123456'

if __name__ == '__main__':
    app.run()