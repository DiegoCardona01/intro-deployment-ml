# Vista que hace la predicción
from .models import PredictionRequest
from .util import get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0] # dado que es un array queremos su valor [0]
    # damos un max(0, prediction) porque no es bueno darle a un usuario final
    # una predicción cruda, en este caso si la predicción nos da negativa ponemos un 0
    # así no confundimos al usuario final en caso de predicciones negativas que analizamos
    # su causa 
    return max(0, prediction)