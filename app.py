from fastapi import FastAPI
from routers.routes import router as predict_router

app = FastAPI(
    title="Loan Default Prediction API",
    description="Production-ready ML API for predicting loan default risk",
    version="1.0.0"
)



@app.get("/")
def health_check():
    return {"status": "healthy"}



app.include_router(predict_router)