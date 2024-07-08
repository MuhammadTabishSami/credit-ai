# Importing Libraries
import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

application = FLask(__name__)

app = application #creating app variable

# Route for homepage
@app.route('/')
def index():
    return render_template('index_html')

@app.route('/predictdata',method=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        pass
     


