from fastapi import APIRouter
from app.schemas import health
from app.schemas import predict_schema
from config import settings
from app import __version__
from structures import __version__ as model_version
import pandas as pd
from fastapi.encoders import jsonable_encoder
from structures.predict import make_prediction
from typing import Any
router = APIRouter()

@router.get('/health',response_model=health.Health, status_code=200)
async def get_health()-> dict:
    health_ = health.Health(project_name = settings.PROJECT_NAME,version = __version__,model_version = model_version)
    return health_.dict()

@router.post('/prediction',status_code=200)
def get_predictions(input_data : predict_schema.input_schema):
    input_to_model = pd.DataFrame(jsonable_encoder(input_data.inputs))
    output = make_prediction(input_to_model)
    return {"predictions" : output['predictions'][0].item(),"errors":output['errors']}

