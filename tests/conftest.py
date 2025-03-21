import pytest
import yaml
import logging
from framework.data_validator import DataValidator
from framework.data_extractor import DataExtractor
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def pytest_configure(config):
    """Ensure reports directory exists before test execution"""
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

def pytest_html_report_title(report):
    """Customize the title of the HTML report"""
    report.title = "🔥 Automated Test Report - Snowflake Framework 🔥"

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Add custom metadata to the test report"""
    prefix.extend([
        "<p><strong>Project:</strong> Snowflake Data Test Framework</p>",
        "<p><strong>Test Environment:</strong> Production</p>",
        "<p><strong>Tester:</strong> Your Name</p>"
    ])

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture(scope="module")
def data_validator():
    """Fixture to initialize DataValidator"""
    return DataValidator(
        source_path=config["source_file"],
        raw_query="SELECT * FROM raw_layer_table WHERE ingestion_date BETWEEN '2023-01-01' AND '2023-12-31'",
        target_query="SELECT * FROM target_table"
    )

@pytest.fixture(scope="module")
def source_data():
    """Fixture to load source test data from file"""
    return DataExtractor.load_source_data(config["source_file"])

@pytest.fixture(scope="module")
def raw_layer_data(data_validator):
    """Fixture to fetch raw layer data from Snowflake"""
    return data_validator.fetch_raw_data()

@pytest.fixture(scope="module")
def target_data(data_validator):
    """Fixture to fetch transformed target data from Snowflake"""
    return data_validator.fetch_target_data()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Hook to log test session start"""
    logging.info("==== Starting Pytest Session ====")

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Hook to log test session completion"""
    logging.info("==== Pytest Session Finished ====")
