from flask import Flask, flash, redirect, render_template, request, session, url_for, make_response
from flask_session import Session
from functionfit import yupdate, polycntm, specfit
from mathutils import gaussian, lorentzian
from getdata import getdata
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

# Configure application
app = Flask(__name__)
app.secret_key = "key"

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure responses aren't cached
@app.after_request
def after_request(response):
	response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	response.headers["Expires"] = 0
	response.headers["Pragma"] = "no-cache"
	return response

# Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		file = request.files['file']
		funcname = request.form.get("function")
		#Saving the uploaded file so that get data could work on it
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		#Getdata parses through the txt file and 
		xdata,ydata = getdata(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		
		#Setting the function to fit to the data
		if funcname == "gaussian":
			func = gaussian
		if funcname == "lorentzian":
			func = lorentzian
		
		#Returns a polynomial object ctnm and the parameters for the function fit to the data
		cntm, fparams = specfit(xdata,ydata,funct=func)
		#Unloads the polynomial cntm and calculates what the y values are for xdata
		baseline = cntm.coef[1]*xdata + cntm.coef[0]

		#Gettin the parameters of the function fit to the data
		param1 = fparams[0]
		param2 = fparams[1]
		param3 = fparams[2]
		#Creates the y values for the function over the baseline
		functdata = func(xdata,*fparams) + baseline
		plt.figure()
		#Uses matplotlib to make a plot of the original data
		plt.plot(xdata,ydata)		
		#Uses matplotlib to make a plot of the function fit
		plt.plot(xdata,functdata, 'r-')
		#Uses matplotlib to make a plot of the baseline data
		plt.plot(xdata,baseline, 'k-')
		#Titles the graph with the parameters obtained from specfit
		plt.title("A = {} mu = {} sigma = {}".format(param1,param2,param3))
		#Axis Labels
		plt.xlabel('lambda (microns)')
		plt.ylabel('Flambda (Normalized)')

		#Saves the graph and gets it ready for a response
		figfile = BytesIO()
		plt.savefig(figfile, format='png')
		figfile.seek(0)
		response=make_response(figfile.getvalue())
		response.headers['Content-Type'] = 'image/png'
		return response
	else:
		return render_template("home.html")

if __name__ == '__main__':
	app.debug = True
	app.run()

