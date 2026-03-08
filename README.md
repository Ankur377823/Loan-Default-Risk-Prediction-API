# Loan Default Risk Prediction API

A production-ready Machine Learning API built using **FastAPI** that
predicts whether a loan will be **Fully Paid or Charged Off** based on
borrower financial and credit features.

This project demonstrates an **end-to-end machine learning deployment
pipeline** including model training, feature engineering,
explainability, logging, and containerized API deployment.

------------------------------------------------------------------------

## Project Overview

Financial institutions need accurate tools to evaluate borrower risk
before approving loans. This project uses a trained ML model to predict
the probability of loan default based on borrower credit and financial
attributes.

The system exposes a **REST API built with FastAPI** that allows
real-time prediction requests.

Each prediction request: - Validates input using **Pydantic schemas** -
Generates a **unique request ID (UUID)** - Logs request details -
Returns prediction probabilities and feature explanations

------------------------------------------------------------------------

## Key Features

-   Loan default prediction using ML model
-   FastAPI production-ready REST API
-   Pydantic input validation
-   Structured logging system
-   SHAP-based explainability
-   UUID tracking for every request
-   Docker containerization
-   Modular and scalable project architecture

------------------------------------------------------------------------

## Tech Stack

**Languages & Frameworks** - Python - FastAPI - Uvicorn

**Machine Learning** - Scikit-learn - Pandas - NumPy - SHAP

**Deployment** - Docker - GitHub - REST API

------------------------------------------------------------------------

## Project Structure

loan-default-api │ ├── app.py ├── requirements.txt │ ├── config │ └──
validators.py │ ├── model │ ├── loan_model_1.pkl │ ├── model_loader.py │
└── predict.py │ ├── routers │ └── routes.py │ ├── schemas │ ├──
user_input.py │ └── prediction_response.py │ ├── utils │ └── logger.py │
└── notebooks └── model.ipynb

------------------------------------------------------------------------

## API Endpoints

### Health Check

GET /

Response: { "status": "healthy" }

------------------------------------------------------------------------

### Loan Default Prediction

POST /predict

Example Request

{ "loan_amnt": 9.92, "term": 60, "int_rate": 21.49, "installment":
557.53, "grade": "D", "sub_grade": "D5", "purpose": "credit_card",
"application_type": "Individual", "annual_inc": 11.25, "dti": 29.27,
"verification_status": "Verified", "home_ownership": "mortgage",
"emp_length": "10+ years" }

Example Response

{ "request_id": "example-uuid", "model_version": "1.0.0", "prediction":
"Fully Paid", "confidence": 0.82 }

------------------------------------------------------------------------

## Running the Project Locally

Install dependencies

pip install -r requirements.txt

Run API

uvicorn app:app --reload

Open API docs

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Docker Deployment

Build image

docker build -t loan-default-api .

Run container

docker run -p 8000:8000 loan-default-api

------------------------------------------------------------------------

## Author

Ankur Kumar Singh\
Civil Engineering Student -- NIT Calicut\
Interested in AI, Machine Learning, and Software Engineering
