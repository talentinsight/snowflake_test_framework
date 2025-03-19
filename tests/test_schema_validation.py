import pytest


@pytest.mark.usefixtures("source_data", "raw_layer_data")
def test_schema_validation_source_raw(source_data, raw_layer_data):
    """Test schema validation between source and raw layer"""
    assert set(source_data.columns) == set(raw_layer_data.columns), "Schema mismatch between source and raw layer"

@pytest.mark.usefixtures("raw_layer_data", "target_data")
def test_schema_validation_raw_target(raw_layer_data, target_data):
    """Test schema validation between raw layer and target layer"""
    assert set(raw_layer_data.columns) == set(target_data.columns), "Schema mismatch between raw layer and target"
