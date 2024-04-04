"""
    This module contains the positive test case class for the dropdown field in the form page
    
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
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from test_data.FormPageDataPositive import FormPageDataPositive
from typing import Dict
from _pytest.fixtures import FixtureRequest
import logging

class TestFormPageDropdownPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    def test_dropdown_years_of_exp_positive(self, get_data: Dict):
        # Method retrieves dropdown element for years of experience and 
        # selects the appropriate value specified in test_data.FormPageDataPositive.
        # Then it checks that the user's option is correctly selected by verifying value from get_data["years_of_exp"]
        # falls in the option selected. i.e. if get_data["years_of_exp"] equals 4 then it must fall in the option 2-4
        # and 2-4 is the selected option
        
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        logger.info("Selecting years of experience from drop down for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        dropdown: WebElement = Select(form_page.retrieve_loc_select_years_of_exp())
        displayed_value:str = dropdown.first_selected_option.text # gets selected option
        
        logger.info("Asserting value of selected years of experience for " + get_data["years_of_exp"] + " years")
        left_bound: int = -float('inf')
        right_bound: int = -float('inf')
        curr_str: str = ""
        for i in range(len(displayed_value)):
            if (displayed_value[i].isdigit()):
                curr_str += displayed_value[i]
            else:
                left_bound = int(curr_str)
                curr_str = ""
        
        if curr_str != "": 
            right_bound = int(curr_str)
            assert  left_bound <= int(get_data["years_of_exp"]) <= right_bound
        else:
            assert int(get_data["years_of_exp"]) >= left_bound
            
        