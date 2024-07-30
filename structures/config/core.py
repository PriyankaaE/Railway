import os
from pathlib import Path
import structures
from pydantic import BaseModel
from typing import Dict, List, Optional, Sequence
from strictyaml import YAML, load


PACKAGE_DIR = Path(structures.__file__).parent
REPO_DIR = PACKAGE_DIR.parent
DATASET_DIR = PACKAGE_DIR / 'Datasets'
CONFIG_PATH = PACKAGE_DIR / 'config.yml'
MODEL_SAVE_DIR = PACKAGE_DIR / 'models'

class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    train_file: str
    test_file: str
    save_name: str

class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    target: str
    features: List[str]
    test_size: float
    categorical_variables: List[str]
    numerical_variables: List[str]
    datatypes: Dict[str, str]
    cabin_vars: str

class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_param_config: ModelConfig

def find_config_file() -> Path:
    """Locate the configuration file."""
    if CONFIG_PATH.is_file():
        return CONFIG_PATH
    raise Exception(f"Config not found at {CONFIG_PATH!r}")

def fetch_config_from_yaml(cfg_path: Optional[Path] = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")

def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_param_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()
