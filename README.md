# Snowflake Test Framework

## Overview
The **Snowflake Test Framework** is a modular and scalable test automation framework designed to validate data ingestion and transformation processes in Snowflake. It ensures data integrity from source files (CSV, JSON, TXT) to the raw layer and then to transformed target layers (Prep/Mart) in Snowflake.

## Features
- **Schema Validation**: Ensures that source and target schemas match.
- **Row Count Validation**: Compares row counts between different layers.
- **Data Consistency Checks**: Verifies that transformed data is accurate.
- **Anomaly Detection**: Identifies data anomalies based on configurable thresholds.
- **Configurable Rules**: Supports flexible validation logic via `config.yaml`.
- **CI/CD Integration**: Designed for integration with Jenkins/GitHub Actions.

## Project Structure
```
snowflake_test_framework/
│── config.yaml
│── main.py
│── README.md
│── tests/
│   ├── test_data_validation.py
│   ├── test_schema_validation.py
│   ├── test_row_count_validation.py
│   ├── test_anomaly_detection.py
│── framework/
│   ├── __init__.py
│   ├── snowflake_connector.py
│   ├── data_extractor.py
│   ├── data_validator.py
│── utils/
│   ├── __init__.py
│   ├── logger.py
│── requirements.txt
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/talentinsight/snowflake_test_framework.git
   cd snowflake_test_framework
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
Update `config.yaml` with the correct Snowflake connection parameters and validation rules.

## Running Tests
Run all tests using:
```sh
pytest tests/
```
Run a specific test:
```sh
pytest tests/test_schema_validation.py
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
MIT License