# from structures.train import config_dict
from structures.config.core import config
from pydantic import BaseModel, ValidationError
import numpy as np
from typing import List, Optional, Tuple

def validate_inputs(input_data):


    relevant_data = input_data[config.model_param_config.categorical_variables + config.model_param_config.numerical_variables].copy()
    # validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleTitanicDataInputs(
            inputs=relevant_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return relevant_data, errors

class TitanicDataInputschema(BaseModel):
    pclass : Optional[float]
    sex : Optional[str]
    age : Optional[float]
    sibsp : Optional[float]
    parch : Optional[float]
    fare : Optional[float]
    cabin : Optional[str]
    embarked : Optional[str]
    title : Optional[str]

class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputschema]