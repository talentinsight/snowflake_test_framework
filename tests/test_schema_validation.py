from framework.data_validator import DataValidator
import pytest
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture(scope="module")
def data_validator():
    return DataValidator(
        source_path=config["source_file"],
        raw_query="SELECT * FROM raw_layer_table WHERE ingestion_date BETWEEN '2023-01-01' AND '2023-12-31'",
        target_query="SELECT * FROM target_table"
    )

@pytest.fixture(scope="module")
def source_data():
    return data_validator().load_source_data(config["source_file"])

@pytest.fixture(scope="module")
def raw_layer_data(data_validator):
    return data_validator.fetch_raw_data()

def test_schema_validation(source_data, raw_layer_data):
    validator = DataValidator(config["source_file"], "", "")
    validator.validate_schema(source_data, raw_layer_data)
