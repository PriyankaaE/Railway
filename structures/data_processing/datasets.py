import pandas as pd
from . import feature_engineer
import numpy as np
import pickle as pkl
import joblib
import os
from structures.config import core
from structures.config.core import config
from structures import __version__ as _version
import typing as t
from sklearn.pipeline import Pipeline
def prepare_dataset(filename:str) -> pd.DataFrame:
    data = data_load(filename)
    data = replace_nan(data)
    data = get_new_columns(data)
    data = change_dtypes(data, col_list=config.model_param_config.datatypes)
    data = data[config.model_param_config.features]
    print(data.shape, data.columns,data.head())
    return data

def data_load(filename : str) -> pd.DataFrame:
    # print('core.dataset ',core.DATASET_DIR,'--',filename)
    data = pd.read_csv(os.path.join(core.DATASET_DIR,filename))
    # data = data[config_dict['features']]
    return data

def replace_nan(data : pd.DataFrame) -> pd.DataFrame:
    data = data.replace('?', np.nan)
    return data

def get_new_columns(data : pd.DataFrame) -> pd.DataFrame:

    data = feature_engineer.get_cabin_data(data, column_name='cabin')
    data = feature_engineer.get_title_column(data, column_name='name', new_column_name='title')
    return data

def change_dtypes(data : pd.DataFrame , col_list: t.List[str]):

    for col_name in col_list:
        data = feature_engineer.change_dtype(data , col_name, col_list[col_name][0])

    return data

def save_pipeline(pipeline_to_persist ,config) -> None:

    save_name = config.app_config.save_name+'_'+ str(_version)+'.pkl'
    save_path = os.path.join(core.MODEL_SAVE_DIR , save_name)
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(config) -> Pipeline:
    save_name = config.app_config.save_name +'_'+ str(_version)+ '.pkl'
    save_path = os.path.join(core.MODEL_SAVE_DIR, save_name)
    loaded_model = joblib.load(save_path)
    return loaded_model


