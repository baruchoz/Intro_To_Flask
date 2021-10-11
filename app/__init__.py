from flask import Flask 


app = Flask(__name__) # from app folder run __init__.py

from app import routes

