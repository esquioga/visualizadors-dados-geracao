from flask import Flask, render_template
import data_access

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', infos=data_access.getOutorgaJSON())

	
	