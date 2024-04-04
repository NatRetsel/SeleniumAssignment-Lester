"""
    This module contains the positive test case class for the checkbox fields in the form page
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


class TestFormPageChkPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    def test_chk_sex_positive(self, get_data: Dict):
        # Method retrieves checkbox element for sex and 
        # selects the appropriate value specified in test_data.FormPageDataPositive.
        # Then it checks that the correct box is selected and the others are not
        
        logger: logging.Logger = self.getLogger()
        fields: set = {"Male", "Female", "Prefer not to say"}
        
        form_page:FormPage = FormPage(self.driver)
        
        logger.info("Selecting sex checkbox for: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        logger.info("Asserting only the correct sex is selected")
        for field in fields:
            if (field != get_data["sex"]):
                assert not form_page.retrieve_loc_chkSex().find_element(By.XPATH, "div[normalize-space()='"+field+"']/input").is_selected() and form_page.retrieve_loc_chkSex().find_element(By.XPATH, "div[normalize-space()='"+field+"']/input").is_selected()
            
                
        # Refreshes the page for other test cases / data
        self.driver.refresh()