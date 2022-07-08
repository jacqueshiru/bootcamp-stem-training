from flask import Flask
app = Flask(__name__)

# Create View 
@app.route("/")
def home():
    return "Flask"