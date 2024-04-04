"""
    This module contains the positive test case class for the text input fields in the form page.
    This assumes user inputs are positive and valid
    - We will check that valid fields input by the user reflects as is on the fields
        - first name
        - last name
        - Job title
        - datepicker through text
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataPositive: List[Dict]
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""
import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from test_data.FormPageDataPositive import FormPageDataPositive
from _pytest.fixtures import FixtureRequest
from typing import Dict
import logging

class TestFormPageTxTPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    
    def test_txt_first_name_positive(self, get_data: Dict):
        # Method gets webelement for first name text input
        # and fills in the first name then checks if input value is the same as provided value
        
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate first name
        logger.info("Populating first name: " + get_data["first_name"])
        form_page.retrieve_loc_txt_first_name().send_keys(get_data["first_name"])
        
        # assert correct value was inputed and reflected
        logger.info("Asserting displayed text equals " + get_data["first_name"])
        assert form_page.retrieve_loc_txt_first_name().get_attribute('value') == get_data["first_name"]
        
        # clear the field
        form_page.retrieve_loc_txt_first_name().clear()
    
    
    def test_txt_last_name_positive(self, get_data: Dict):
        # Method gets webelement for last name text input
        # and fills in the last name then checks if input value is the same as provided value
        
        logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate last name
        logger.info("Populating last name: " + get_data["last_name"])
        form_page.retrieve_loc_txt_last_name().send_keys(get_data["last_name"])
        
        # assert correct value was inputed and reflected
        logger.info("Asserting displayed text equals " + get_data["last_name"])
        assert form_page.retrieve_loc_txt_last_name().get_attribute('value') == get_data["last_name"]
        
        # clear the field
        form_page.retrieve_loc_txt_last_name().clear()
        
    def test_txt_job_title_positive(self, get_data):
        # Method gets webelement for job title text input
        # and fills in the job title then checks if input value is the same as provided value
        
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate job title
        logger.info("Populating job title: " + get_data["job_title"])
        form_page.retrieve_loc_txt_job_title().send_keys(get_data["job_title"])
        
        # assert correct value was inputed and reflected
        logger.info("Asserting displayed text equals " + get_data["job_title"])
        assert form_page.retrieve_loc_txt_job_title().get_attribute('value') == get_data["job_title"]
        
        # clear the field
        form_page.retrieve_loc_txt_job_title().clear()
        
    def test_txt_datepicker_positive(self, get_data):
        # Method gets webelement for datepicker text input
        # and fills in the date of birth then checks if input value is the same as provided value
        
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate date 
        logger.info("Populating date: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        logger.info("Asserting displayed text equals " + get_data["date_of_birth"])
        assert form_page.retrieve_loc_txt_dt_datepicker().get_attribute('value') == get_data["date_of_birth"]
        # clear the field
        form_page.retrieve_loc_txt_dt_datepicker().clear()