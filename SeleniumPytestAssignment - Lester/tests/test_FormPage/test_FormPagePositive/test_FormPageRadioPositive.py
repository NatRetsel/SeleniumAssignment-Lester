"""
    This module contains the positive test case class for the radio fields in the form page
    This assumes user inputs are positive and valid
        - User checks the correct button at first try and checks only one button
    We will validate that the button value checked is indeed what the user intended, specified 
    in test_data.FormPageDataPositive: List[Dict].
    
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataPositive: List[Dict]
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""
import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from selenium.webdriver.common.by import By
from test_data.FormPageDataPositive import FormPageDataPositive
from _pytest.fixtures import FixtureRequest
from typing import Dict
import logging


class TestFormPageRadioBtnPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    def test_radio_highest_edu_level_positive(self, get_data: Dict):
        # Method retrieves radio element for highest education level and 
        # selects the appropriate level of education specified in test_data.FormPageDataPositive.
        # Then it checks that the correct button is selected and the others are not
        fields:set = {"High School", "College", "Grad School"}
        logger: logging.Logger = self.getLogger()
        
        form_page:FormPage = FormPage(self.driver)
        logger.info("Selecting radio button for highest education level: " + get_data["edu_level"])
        self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), get_data["edu_level"])
             
        logger.info("Asserting radio button selection for highest education level: " + get_data["edu_level"])
        for field in fields:
            if (field != get_data["edu_level"]):
                assert not form_page.retrieve_loc_radio_edu_level().find_element(By.XPATH, "div[normalize-space()='"+field+"']/input").is_selected() and form_page.retrieve_loc_radio_edu_level().find_element(By.XPATH, "div[normalize-space()='"+get_data["edu_level"]+"']/input").is_selected()
            
        
        # Refreshes the page for other test cases / data
        self.driver.refresh()
        