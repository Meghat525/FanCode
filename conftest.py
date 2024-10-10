import sys
import os
import logging
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Configure the logger
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level here
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("test_log.log"),  # Log to a file
            logging.StreamHandler()  # Also log to the console
        ]
    )

@pytest.fixture
def logger():
    return logging.getLogger(__name__)