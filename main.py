from flask import Flask, render_template
from data_access import getOutorgas

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', infos=getOutorgas())

	
	