from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ('home.html')

@app.route("/projects")
def projects():
	return('projects.html')