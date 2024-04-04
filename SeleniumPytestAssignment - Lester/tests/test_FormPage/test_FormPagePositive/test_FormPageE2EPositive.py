"""
    This module contains the end to end positive test case class for the form page.
    - this assumes the user selects exactly one radio button and one checkbox for each query and 
    selects a valid date.
    - the end to end assertion will check
        - form can be submitted and success message is shown
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

class TestFormPagePositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    def test_e2e_positive(self, get_data: Dict):
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate first name
        logger.info("Populating first name: " + get_data["first_name"])
        form_page.retrieve_loc_txt_first_name().send_keys(get_data["first_name"])
        
        # populate last name
        logger.info("Populating last name: " + get_data["last_name"])
        form_page.retrieve_loc_txt_last_name().send_keys(get_data["last_name"])
        
        # populate job title
        logger.info("Populating job title: " + get_data["job_title"])
        form_page.retrieve_loc_txt_job_title().send_keys(get_data["job_title"])
        
        # select radio option
        logger.info("Selecting radio button on highest education level: " + get_data["edu_level"])
        self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), get_data["edu_level"])
        
        # select sex checkbox
        logger.info("Selecting sex checkbox: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        # select YOE drop down
        logger.info("Selecting years of experience dropdown for: " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Populating date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        # click submit button
        logger.info("Submitting...")
        form_page.retrieve_loc_btn_submit().click()
        
        # Assert success message is seen on the alert element
        logger.info("Asserting alert message")
        assert "success" in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()
        
