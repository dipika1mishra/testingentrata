import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.chrome.webdriver.WebDriver(executable_path=r"C:\chromedriver-win64 version 120\chromedriver.exe")
@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver (Chrome in this example)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown - quit WebDriver
    driver.quit()

def test_homepage_title(driver):
    # Open the entrata.com homepage
    driver.get("https://www. .com/")
    # Verify the title of the homepage
    assert "Entrata" in driver.title

def test_navigation_to_solutions(driver):
    # Open the entrata.com homepage
    driver.get("https://www.entrata.com/")
    # Click on the Solutions link in the navigation menu
    solutions_link = driver.find_element(By.LINK_TEXT, "Solutions")
    solutions_link.click()
    # Verify the title of the Solutions page
    WebDriverWait(driver, 10).until(EC.title_contains("Solutions"))
    assert "Solutions" in driver.title

def test_contact_form_interaction(driver):
    # Open the entrata.com homepage
    driver.get("https://www.entrata.com/")
    # Click on the Contact link in the footer
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()
    # Interact with the contact form (without submitting)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    name_input = driver.find_element(By.NAME, "name")
    name_input.send_keys("John Doe")
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("john.doe@example.com")
    message_input = driver.find_element(By.NAME, "message")
    message_input.send_keys("This is a test message.")
    # Verify that form fields are filled correctly
    assert name_input.get_attribute("value") == "John Doe"
    assert email_input.get_attribute("value") == "john.doe@example.com"
    assert message_input.get_attribute("value") == "This is a test message."

if _name_ == "_main_":
    pytest.main()