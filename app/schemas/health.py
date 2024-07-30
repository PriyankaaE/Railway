from pydantic import BaseModel

class Health(BaseModel):
    project_name : str
    version : str
    model_version : str