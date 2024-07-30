import numpy as np
import re
def get_first_cabin(row):
    try:
        return row.split()[0]
    except:
        return np.nan

def get_cabin_data(data , column_name):
    data[column_name] = data[column_name].apply(get_first_cabin)
    return data


def get_title(passenger):
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'

def get_title_column(data,column_name , new_column_name):

    data[new_column_name] = data[column_name].apply(get_title)
    return data

def change_dtype(data , col_name , col_dtype):
    # print(col_name,col_dtype)
    data[col_name] = data[col_name].astype(col_dtype)
    return data