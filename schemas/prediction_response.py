from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):

    model_version: str = Field(
        ...,
        description="Version of the deployed ML model",
        example="1.0.0"
    )

    prediction: str = Field(
        ...,
        description="Predicted loan status",
        example="Fully Paid"
    )

    default_probability: float = Field(
        ...,
        description="Probability of default",
        example=0.41
    )

    confidence: float = Field(
        ...,
        description="Confidence score of predicted class",
        example=0.72
    )

    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across classes",
        example={
            "Charged Off": 0.41,
            "Fully Paid": 0.59
        }
    )

    top_features_influencing_prediction: Dict[str, float] = Field(
        ...,
        description="Top SHAP features influencing prediction",
        example={
            "int_rate": 0.32,
            "dti": 0.21,
            "loan_income_ratio": 0.14,
            "bc_util": 0.09,
            "inq_last_6mths": 0.06
        }
    )

    class Config:
        json_schema_extra = {
            "example": {
                "model_version": "1.0.0",
                "prediction": "Fully Paid",
                "default_probability": 0.23,
                "confidence": 0.77,
                "class_probabilities": {
                    "Charged Off": 0.23,
                    "Fully Paid": 0.77
                },
                "top_features_influencing_prediction": {
                    "int_rate": 0.32,
                    "dti": 0.21,
                    "loan_income_ratio": 0.14,
                    "bc_util": 0.09,
                    "inq_last_6mths": 0.06
                }
            }
        }