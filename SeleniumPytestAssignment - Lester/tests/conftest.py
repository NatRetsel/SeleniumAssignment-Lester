"""
    This module contains the fixtures for the page testing.
"""
import pytest
from selenium import webdriver
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser) -> None:
    # adding options to store command line arguments to be used in setup fixture
    # (key), default_value, help (optional text)
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--uri", action="store", default="https://formy-project.herokuapp.com/form")


@pytest.fixture(scope="class")
def setup(request: FixtureRequest):
    """
        This fixture contains the setup and teardown methods for driver initiation and closing. Scope is tied
        to the entire test session. A parser is introduced to allow browser selection through command line parameters.
        
        parameters: request: FixtureRequest - an instance of the fixture to be inherited by a base class to access
        the webdriver.
    """
    browser:str = request.config.getoption("browser_name")
    test_uri:str = request.config.getoption("uri")
    
    match browser.lower():
        case "chrome":
            driver = webdriver.Chrome()
        case "firefox":
            driver = webdriver.Firefox()
        case "edge":
            driver = webdriver.Edge()
        case "safari":
            driver = webdriver.Safari()
        case _: #defaults to Chrome
            driver = webdriver.Chrome()
    
    #if elements don't show up, driver will wait at most 5s for it before concluding element missing
    driver.implicitly_wait(5) 
    driver.get(test_uri)
    
    #assigned as a class variable so classes using this fixture can reference driver via self.driver
    request.cls.driver = driver 
    
    yield
    driver.close() #teardown

