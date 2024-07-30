import pandas as pd
import typing as t

# from feature_engineering import datasets
from structures.config.core import config
# import yaml
from structures import pipeline_fit
from structures.data_processing.validate import validate_inputs
from structures.data_processing.datasets import load_pipeline
# config_file = core.CONFIG_PATH
# with open(config_file) as f:
#     config_dict = yaml.safe_load(f)
_previous_pipe = load_pipeline(config)
# print(_previous_pipe)
def make_prediction(input_data:t.Union[pd.DataFrame, dict]) -> dict:

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data = data)
    results = {"predictions":None , "errors" : errors}
    print('errors ',errors)
    if not errors:
        predictions = _previous_pipe.predict(X = validated_data[config.model_param_config.features[:-1]])

        results = {"predictions": predictions, "errors": errors}
    # else:
    #     results = {"predictions": [], "errors": errors}
    print('results ',results)
    return results
