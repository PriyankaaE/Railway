import os
from pathlib import Path
from Production_packaging import Pipeline

PACKAGE_DIR = Path(Pipeline.__file__).parent
REPO_DIR = PACKAGE_DIR.parent
DATASET_DIR = PACKAGE_DIR + '/Datasets'
CONFIG_PATH = PACKAGE_DIR + '/config.yml'


