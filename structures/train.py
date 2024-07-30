from data_processing import datasets
from structures.config import core
from structures.config.core import config
# import yaml
from sklearn.model_selection import train_test_split
from pipeline_fit import titanic_pipe

def run_training() -> None:
    data = datasets.prepare_dataset(config.app_config.train_file)
    data['pclass'] = data['pclass'].astype('str')
    data['pclass'] = data['pclass'].astype('O')
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.model_param_config.target, axis=1),  # predictors
        data[config.model_param_config.target],  # target
        test_size=float(config.model_param_config.test_size),  # percentage of obs in test set
        random_state=0)

    # titaninc_fit = pipeline_fit.train(config_dict)
    # titanic_fit = pipeline_fit.titanic_pipe
    titanic_pipe.fit(X_train , y_train)
    datasets.save_pipeline(titanic_pipe , config)
    print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

if __name__ == "__main__":
    run_training()



