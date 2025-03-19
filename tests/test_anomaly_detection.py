import pytest
from conftest import source_data, raw_layer_data, target_data

@pytest.mark.usefixtures("raw_layer_data")
def test_anomaly_detection_raw(raw_layer_data):
    """Test anomaly detection in raw layer"""
    threshold = 3
    for column in raw_layer_data.select_dtypes(include=["number"]):
        mean, std = raw_layer_data[column].mean(), raw_layer_data[column].std()
        anomalies = raw_layer_data[(raw_layer_data[column] < mean - threshold * std) | 
                                   (raw_layer_data[column] > mean + threshold * std)]
        assert anomalies.empty, f"Anomalies detected in column {column}"

@pytest.mark.usefixtures("target_data")
def test_anomaly_detection_target(target_data):
    """Test anomaly detection in target layer"""
    threshold = 3
    for column in target_data.select_dtypes(include=["number"]):
        mean, std = target_data[column].mean(), target_data[column].std()
        anomalies = target_data[(target_data[column] < mean - threshold * std) | 
                                (target_data[column] > mean + threshold * std)]
        assert anomalies.empty, f"Anomalies detected in column {column}"
