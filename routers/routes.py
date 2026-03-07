from fastapi import APIRouter
from schemas.user_input import LoanApplication
from schemas.prediction_response import PredictionResponse
from model.predict import predict_output

router = APIRouter()



# Prediction Endpoint

@router.post("/predict", response_model=PredictionResponse)
def predict(data: LoanApplication):
    return predict_output(data)



# Model Info Endpoint

@router.get("/model-info")
def model_info():

    return {
        "model_name": "Loan Default Predictor",
        "version": "1.0.0",
        "algorithm": "XGBOOSTClassifier",
        "description": "Predicts whether a loan will be fully paid or charged off"
    }