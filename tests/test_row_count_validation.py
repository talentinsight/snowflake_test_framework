import pytest
from conftest import source_data, raw_layer_data, target_data

@pytest.mark.usefixtures("source_data", "raw_layer_data")
def test_row_count_source_raw(source_data, raw_layer_data):
    """Test row count validation between source and raw layer"""
    assert len(source_data) == len(raw_layer_data), f"Row count mismatch: Source({len(source_data)}) vs Raw Layer({len(raw_layer_data)})"

@pytest.mark.usefixtures("raw_layer_data", "target_data")
def test_row_count_raw_target(raw_layer_data, target_data):
    """Test row count validation between raw layer and target"""
    assert len(raw_layer_data) == len(target_data), f"Row count mismatch: Raw Layer({len(raw_layer_data)}) vs Target({len(target_data)})"
