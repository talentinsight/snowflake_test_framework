import pytest
from conftest import source_data, raw_layer_data, target_data

@pytest.mark.usefixtures("source_data", "raw_layer_data")
def test_data_consistency_source_raw(source_data, raw_layer_data):
    """Test data consistency between source and raw layer"""
    mismatches = (source_data != raw_layer_data).sum().sum()
    assert mismatches == 0, f"Data mismatch detected in {mismatches} cells between source and raw layer"

@pytest.mark.usefixtures("raw_layer_data", "target_data")
def test_data_consistency_raw_target(raw_layer_data, target_data):
    """Test data consistency between raw layer and target"""
    mismatches = (raw_layer_data != target_data).sum().sum()
    assert mismatches == 0, f"Data mismatch detected in {mismatches} cells between raw layer and target"
