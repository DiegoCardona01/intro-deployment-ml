from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os
from io import BytesIO

import pickle

def get_model() -> Pipeline:
    # Variable que recibe de donde viene el modelo, por defecto usamos el model.pkl
    model_path = os.environ.get('MODEL_PATH', 'model/model.pkl')
    with open(model_path, 'rb') as model_file:
        # Transformamos el model_path en bytes y lo cargamos
        model = load(BytesIO(model_file.read()))
    # with open(model_path, 'rb') as model_file:
    #     model = pickle.load(model_file)
    return model

# Transformemos el request en algo que se pueda usar para hacer la predicción
# lo transformamos en dataframe
def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.model_dump().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame