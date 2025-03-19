from framework.snowflake_connector import SnowflakeConnector
import yaml
import pandas as pd

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

class DataValidator:
    def __init__(self, source_path, raw_query, target_query):
        self.source_path = source_path
        self.raw_query = raw_query
        self.target_query = target_query
        self.snowflake = SnowflakeConnector()

    def fetch_raw_data(self):
        return self.snowflake.fetch_data(self.raw_query)

    def fetch_target_data(self):
        return self.snowflake.fetch_data(self.target_query)

    def validate_schema(self, source, target):
        assert set(source.columns) == set(target.columns), "Schema mismatch between source and target"

    def validate_row_count(self, source, target):
        assert len(source) == len(target), f"Row count mismatch: Source({len(source)}) vs Target({len(target)})"

    def validate_data(self, source, target):
        mismatches = (source != target).sum().sum()
        assert mismatches == 0, f"Data mismatch detected in {mismatches} cells"

    def detect_anomalies(self, data):
        threshold = config["anomaly_threshold"]
        for column in data.select_dtypes(include=["number"]):
            mean, std = data[column].mean(), data[column].std()
            anomalies = data[(data[column] < mean - threshold * std) | (data[column] > mean + threshold * std)]
            assert anomalies.empty, f"Anomalies detected in column {column}"
