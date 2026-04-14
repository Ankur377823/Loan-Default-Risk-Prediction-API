import pickle

MODEL_PATH = "loan_model_1.pkl"

class ModelLoader:

    _pipeline = None

    @classmethod
    def load_model(cls):

        if cls._pipeline is None:
            with open(MODEL_PATH, "rb") as f:
                cls._pipeline = pickle.load(f)

        return cls._pipeline
