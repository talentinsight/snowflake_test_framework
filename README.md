# Snowflake Data Test Automation Framework

## Overview
This framework automates data validation for ETL processes using **Python, Pytest, and Pandas**. It ensures data integrity between **source files, raw layers, and transformed target layers** in a Snowflake database.

## Features
- **Schema Validation**: Ensures source, raw, and target data layers match expected structures.
- **Row Count Validation**: Confirms data completeness between transformations.
- **Cell-by-Cell Data Comparison**: Detects discrepancies in raw and transformed data.
- **Anomaly Detection**: Identifies outliers in numeric columns based on standard deviation thresholds.
- **Configurable Validation Rules**: Custom validation logic for different datasets.
- **CI/CD Integration**: Automates tests using Jenkins or GitHub Actions.

## Project Structure
```
snowflake_test_framework/
│── config.yaml
│── main.py
│── README.md
│── tests/
│   ├── conftest.py
│   ├── test_source_data.py       # Source data validation before ingestion
│   ├── test_data_validation.py   # Raw vs. target data consistency checks
│   ├── test_schema_validation.py # Schema structure validation
│   ├── test_row_count_validation.py # Row count verification
│   ├── test_anomaly_detection.py # Outlier detection
│── framework/
│   ├── __init__.py
│   ├── data_extractor.py
│   ├── data_validator.py
│   ├── snowflake_connector.py
│── utils/
│   ├── __init__.py
│   ├── logger.py
│── requirements.txt
```

## Setup Instructions
### **1️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **2️⃣ Configure Snowflake Connection**
Update `config.yaml` with your Snowflake credentials and table settings:
```yaml
snowflake:
  user: "YOUR_SNOWFLAKE_USER"
  password: "YOUR_SNOWFLAKE_PASSWORD"
  account: "YOUR_SNOWFLAKE_ACCOUNT"
  warehouse: "YOUR_WAREHOUSE"
  database: "YOUR_DATABASE"
  schema: "YOUR_SCHEMA"

anomaly_threshold: 3
source_file: "data/source_data.csv"
raw_query: "SELECT * FROM raw_layer_table WHERE ingestion_date BETWEEN '2023-01-01' AND '2023-12-31'"
target_query: "SELECT * FROM target_table"
```

### **3️⃣ Run Tests**
To execute all tests:
```sh
pytest tests/
```
To run specific test files:
```sh
pytest tests/test_source_data.py
```

## CI/CD Integration
- This framework can be integrated with **GitHub Actions** or **Jenkins** for automated validation in deployment pipelines.

## Future Enhancements
- **Test Reporting**: Generate structured reports using `pytest-html`.
- **Extended Data Quality Checks**: Implement more validation rules for business-specific constraints.

---
### **Contributors**
Developed by **[Your Name]**, with expertise in **Python, Pytest, Snowflake, and Data Validation Automation**.
