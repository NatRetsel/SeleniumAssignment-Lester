"""
    This module contains the negative test case class for the dropdown field in the form page
    
    We will validate that the submitted form should not be a success when no selection is made
    to the dropdown field. All other fields will be populated with valid data from 
    test_data.FormPageDataPositive: List[Dict]
    
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataPositive: List[Dict]
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""
import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from test_data.FormPageDataPositive import FormPageDataPositive
from typing import Dict
from pytest_check import check
from _pytest.fixtures import FixtureRequest
import logging

class TestFormPageDropdownNegative(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    def test_dropdown_years_of_exp_negative(self, get_data:Dict):
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
        logger.info("Selecting radio button for highest education level: " + get_data["edu_level"])
        self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), get_data["edu_level"])
        
        # select sex checkbox
        logger.info("Selectiong checkbox for sex: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        # click submit button
        logger.info("Sumitting form without selecting years of experience dropdown")
        form_page.retrieve_loc_btn_submit().click()
        
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()