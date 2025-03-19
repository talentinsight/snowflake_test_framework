import pytest

@pytest.mark.usefixtures("source_data")
def test_source_schema(source_data):
    """Ensure source file schema matches expected structure."""
    expected_columns = ["customer_id", "order_id", "order_date", "amount", "status"]
    assert list(source_data.columns) == expected_columns, "Source data schema mismatch!"

@pytest.mark.usefixtures("source_data")
def test_source_not_null_values(source_data):
    """Ensure critical columns are not null in source data."""
    critical_columns = ["customer_id", "order_id", "amount"]
    for col in critical_columns:
        assert source_data[col].notnull().all(), f"Null values found in column: {col}"

@pytest.mark.usefixtures("source_data")
def test_source_duplicate_primary_keys(source_data):
    """Ensure source data does not contain duplicate primary keys."""
    primary_key = "order_id"
    assert source_data[primary_key].nunique() == len(source_data), f"Duplicate primary keys found in {primary_key}"

@pytest.mark.usefixtures("source_data")
def test_source_accepted_values(source_data):
    """Ensure 'status' column contains only predefined valid values."""
    valid_statuses = {"Pending", "Completed", "Cancelled"}
    assert set(source_data["status"].unique()).issubset(valid_statuses), "Invalid status values detected!"

@pytest.mark.usefixtures("source_data")
def test_source_anomaly_detection(source_data):
    """Detect anomalies in numeric columns before ingestion."""
    threshold = 3  # Standard deviation threshold
    for column in source_data.select_dtypes(include=["number"]):
        mean, std = source_data[column].mean(), source_data[column].std()
        anomalies = source_data[(source_data[column] < mean - threshold * std) | 
                                (source_data[column] > mean + threshold * std)]
        assert anomalies.empty, f"Anomalies detected in column {column}"
