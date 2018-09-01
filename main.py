from flask import Flask, render_template
from data_access import getOutorgas, upsertOutorgaInfo
import datetime as dt

app = Flask(__name__)
upsertOutorgaInfo()
lastUpdate = dt.datetime.now()

@app.route("/")
def index():
	timeDelta = dt.datetime.now() - lastUpdate
	outorgas = getOutorgas()
	if (timeDelta.days > 29) or (not outorgas):
		upsertOutorgaInfo()
		outorgas = getOutorgas()	
	return render_template('index.html', infos=outorgas)

	
	