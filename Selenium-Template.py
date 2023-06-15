import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions object and configure headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the ChromeDriver with the options
driver = webdriver.Chrome(options=chrome_options)


def test_login_logout(browser):
    # Go to the home page
    browser.get("https://practicetestautomation.com/practice-test-login/")
    
    # Verify the home page is displayed correctly
    assert "Example Domain" in browser.title
    
    # Find and click on the "Login" link
    login_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()
    
    # On the login page, enter incorrect data and click the login button
    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    username_input.send_keys("test")
    password_input.send_keys("test")
    login_button.click()
