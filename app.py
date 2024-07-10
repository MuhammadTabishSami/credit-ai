# Importing Libraries
import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application #creating app variable

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            last_fico_range_high=float(request.form.get('last_fico_range_high')),
            last_fico_range_low=float(request.form.get('last_fico_range_low')),
            collection_recovery_fee=float(request.form.get('collection_recovery_fee')),
            total_pymnt_inv=float(request.form.get('total_pymnt_inv')),
            int_rate=float(request.form.get('int_rate')),
            fico_range_high=float(request.form.get('fico_range_high')),
            debt_settlement_flag=request.form.get('debt_settlement_flag'),
            sub_grade=request.form.get('sub_grade'),
            grade=request.form.get('grade'),
            term=request.form.get('term')

        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()   #Initializing Predict Pipeline
        results=predict_pipeline.predict(pred_df) # It will call predict function
        if results == 1:
            results = 'Good Loan'
        else:
            results = 'Bad Loan'
        print(results)
        
        return render_template('home.html',results=results)

if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)

    # The host (0.0.0.0) will map it with (127.0.1) with debug=True


     


