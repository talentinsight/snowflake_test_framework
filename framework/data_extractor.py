import pandas as pd
import os

class DataExtractor:
    @staticmethod
    def load_source_data(file_path):
        file_extension = os.path.splitext(file_path)[-1].lower()
        if file_extension == ".csv":
            return pd.read_csv(file_path)
        elif file_extension == ".json":
            return pd.read_json(file_path)
        elif file_extension == ".txt":
            return pd.read_csv(file_path, delimiter="\t")
        else:
            raise ValueError("Unsupported file format")
