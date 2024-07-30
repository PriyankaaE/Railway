import pytest

from structures.config.core import config
from structures.data_processing.datasets import prepare_dataset


@pytest.fixture()
def sample_input_data():
    return prepare_dataset(config.app_config.test_file)
