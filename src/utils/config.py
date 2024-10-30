import os
from pathlib import Path

PROJECT_DIR_PATH = Path(__file__).parent.parent.parent.resolve()

DATASET_PATH = os.path.join(PROJECT_DIR_PATH, "data\\raw")

KAGGLE_KEY_PATH = os.path.join(PROJECT_DIR_PATH, "src\\utils")