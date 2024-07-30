from sklearn.pipeline import Pipeline

# for the preprocessors
from sklearn.base import BaseEstimator,TransformerMixin

# feature scaling
from sklearn.preprocessing import StandardScaler

# to build the models
from sklearn.linear_model import LogisticRegression

# for imputation
from feature_engine.imputation import (
    CategoricalImputer,
    AddMissingIndicator,
    MeanMedianImputer)

# for encoding categorical variables
from feature_engine.encoding import (
    RareLabelEncoder,
    OneHotEncoder
)
from structures.config.core import config
# import yaml

# from train import config_dict
from structures.data_processing.train_pipeline import ExtractLetterTransformer

# config_file = core.CONFIG_PATH
# with open(config_file) as f:
#     config_dict = yaml.safe_load(f)
# print(config_dict)

# def train(config_dict):
NUMERICAL_VARIABLES = config.model_param_config.numerical_variables
CATEGORICAL_VARIABLES = config.model_param_config.categorical_variables

# set up the pipeline
titanic_pipe = Pipeline([

    # ===== IMPUTATION =====
    # impute categorical variables with string 'missing'
    ('categorical_imputation', CategoricalImputer('missing', variables=CATEGORICAL_VARIABLES)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables=NUMERICAL_VARIABLES)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(imputation_method='median', variables=NUMERICAL_VARIABLES)),

    # Extract first letter from cabin
    ('extract_letter', ExtractLetterTransformer(variable='cabin')),

    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    # ('rare_label_encoder', RareLabelEncoder(tol=0.05, variables=CATEGORICAL_VARIABLES)),

    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(drop_last=True, variables=CATEGORICAL_VARIABLES)),

    # scale using standardization
    ('scaler', StandardScaler()),

    # logistic regression (use C=0.0005 and random_state=0)
    ('Logit', LogisticRegression(C=0.0005, random_state=0)),
])

    # return titanic_pipe

# def predict(pipeline , X_test):
#
#     prediction = pipeline.predict(X_test)
#     return prediction