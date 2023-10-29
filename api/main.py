# Creamos el servicio
from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

#Instanciamos la dirección en local con / para probar el desarrollo
app = FastAPI(docs_url='/')

# Creamos el endpoint para la version 1 del modelo
# este ejecuta mak_model_prediction que es la predicción
@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross=get_prediction(request))