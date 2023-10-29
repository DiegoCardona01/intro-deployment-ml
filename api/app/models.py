# Contiene las características para hacer la predicción y el target que se quiere predecir

# Para serializar los jsons que entran y salen en las peticiones
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    opening_gross : float
    screens : float
    production_budget : float
    title_year : int
    aspect_ratio : float
    duration : int
    cast_total_facebook_likes : float
    budget : float
    imdb_score : float

class PredictionResponse(BaseModel):
    worldwide_gross: float