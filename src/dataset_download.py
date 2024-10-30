import os
from utils.config import DATASET_PATH, KAGGLE_KEY_PATH

os.environ['KAGGLE_CONFIG_DIR'] = KAGGLE_KEY_PATH
print(f"Kaggle config directory set to: {os.environ.get('KAGGLE_CONFIG_DIR')}")

kaggle_json_path = os.path.join(KAGGLE_KEY_PATH, 'kaggle.json')
if not os.path.exists(kaggle_json_path):
    print(f"Error: kaggle.json file not found in {KAGGLE_KEY_PATH}. Please ensure it exists and try again.")
else:
    import kaggle

    if not os.path.exists(DATASET_PATH):
        os.makedirs(DATASET_PATH)
    elif os.listdir(DATASET_PATH):
        print(f"Dataset already exists in {DATASET_PATH}. Skipping download.")
        exit()

    try:
        kaggle.api.dataset_download_files(
            'praffulsingh009/steam-video-games-2024',
            path=DATASET_PATH,
            unzip=True
        )  
        
        print(f"Dataset downloaded successfully to: {DATASET_PATH}")

    except kaggle.api.kaggle_api_extended.KaggleApiError as e:
        print(f"Error downloading dataset: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")