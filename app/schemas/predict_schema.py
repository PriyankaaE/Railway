from pydantic import BaseModel
from typing import List,Any,Optional
from structures.data_processing.validate import TitanicDataInputschema
class Prediction_schema(BaseModel):
    predictions : Optional[Any]
    errors : Optional[Any]

class input_schema(BaseModel):
    inputs : List[TitanicDataInputschema]

