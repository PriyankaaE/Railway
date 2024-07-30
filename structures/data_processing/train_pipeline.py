import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variable : str):
        if not isinstance(variable, str):
            raise ValueError("variables should be a str")

        self.variable = variable

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X[self.variable] = X[self.variable].str.findall("([a-zA-Z]+)").str.join("")
        return X