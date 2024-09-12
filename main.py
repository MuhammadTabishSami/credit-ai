# importing libraries
from fastapi import FastAPI,Request,Form
from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Creating FAST/API instance
app=FastAPI()

# Enabling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://35.178.138.99:3000"],
    # allow_credentials=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# Setting up Jinja2 templates
# templates=Jinja2Templates(directory='templates')

# Define a Pydantic Model for input validation
class PredictData(BaseModel):
    last_fico_range_high: float
    last_fico_range_low: float
    collection_recovery_fee: float
    total_pymnt_inv: float
    int_rate: float
    fico_range_high: float
    debt_settlement_flag: str
    sub_grade: str
    grade: str
    term: str

    def to_custom_data(self):
        return CustomData(
            last_fico_range_high=self.last_fico_range_high,
            last_fico_range_low=self.last_fico_range_low,
            collection_recovery_fee=self.collection_recovery_fee,
            total_pymnt_inv=self.total_pymnt_inv,
            int_rate=self.int_rate,
            fico_range_high=self.fico_range_high,
            debt_settlement_flag=self.debt_settlement_flag,
            sub_grade=self.sub_grade,
            grade=self.grade,
            term=self.term
        )

# Route for testing server
@app.get("/")
async def read_root():
    return {"message": "Welcome to the prediction API. Use POST /predictdata to get predictions."}

# Route for prediction
@app.post('/predictdata')
async def predict_datapoint(data: PredictData):
    try:
        
        # Convert PredictData to CustomData instance
        custom_data = data.to_custom_data()
        pred_df = custom_data.get_data_as_data_frame()
        print(pred_df)

        # Initialize Predict Pipeline and make predictions
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Interpret the results
        result_text = 'Good Loan' if results == 1 else 'Bad Loan'
        print(result_text)

        # Return the prediction result as JSON
        return {"result": result_text}
    
    except Exception as e:
        print(f'Prediction Error: {str(e)}')
        return JSONResponse(status_code=500,content={'message':"Prediction failed, Please try again later."})
    
@app.options("/predictdata")
async def options_predictdata():
    return JSONResponse(
        status_code=200,
        content={"message": "CORS Preflight Request"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)
