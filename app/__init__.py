from flask import Flask 
from config import Config


app = Flask(__name__) # from app folder run __init__.py
app.config.from_object(Config) 


from app import routes

