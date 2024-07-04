import pandas as pd
from Pipeline.config import core
import yaml

config_file = core.CONFIG_PATH
with open(config_file) as f:
    config_dict = yaml.safe_load(f)

def data_load():

    data = pd.read_csv(core.DATASET_DIR)
    data = data[config_dict.features]
    return data

