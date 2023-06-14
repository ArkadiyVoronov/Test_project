import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions object and configure headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the ChromeDriver with the options
driver = webdriver.Chrome(options=chrome_options)

@pytest.fixture
def browser():
