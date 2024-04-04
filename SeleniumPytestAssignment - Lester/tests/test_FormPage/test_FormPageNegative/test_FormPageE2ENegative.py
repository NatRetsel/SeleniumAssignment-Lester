"""
    This module contains the end to end negative test case class for the form page.
    We will assume the date field means the date of birth
    Negative test cases:
        - user might choose a future date of birth than current date
        - user may select more than one radio button
        - user may select more than one check box
    - the end to end assertion will therefore check
        - that form shouldn't be successfully submitted 
            - verify with the alert, success should be appearing
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataPositive: List[Dict]
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""
import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from test_data.FormPageDataNegative import FormPageDataNegative
from pytest_check import check
from typing import Dict
from _pytest.fixtures import FixtureRequest
import logging

class TestFormPageNegative(BaseClass):
    
    @pytest.fixture(params=FormPageDataNegative.test_form_data)
    def get_neg_data(self, request: FixtureRequest):
        return request.param
    
    def test_e2e_negative(self, get_neg_data: Dict):
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate first name
        logger.info("Populating first name: " + get_neg_data["first_name"])
        form_page.retrieve_loc_txt_first_name().send_keys(get_neg_data["first_name"])
        
        # populate last name
        logger.info("Populating last name: " + get_neg_data["last_name"])
        form_page.retrieve_loc_txt_last_name().send_keys(get_neg_data["last_name"])
        
        # populate job title
        logger.info("Populating job title: " + get_neg_data["job_title"])
        form_page.retrieve_loc_txt_job_title().send_keys(get_neg_data["job_title"])
        
        # select radio option
        # first check that it is not empty
        logger.info("Selecting radio button for highest education level: " + str(get_neg_data["edu_level"]))
        if get_neg_data["edu_level"]:
            for option in get_neg_data["edu_level"]:
                self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), option)
        
        # select sex checkbox
        # first check that it is not empty
        logger.info("Selectiong checkbox for sex: " + str(get_neg_data["sex"]))
        if get_neg_data["sex"]:
            for option in get_neg_data["sex"]:
                self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), option)
        
        # select YOE drop down
        # first check that it is not empty string
        logger.info("Selecting years of experience from dropdown for " + get_neg_data["years_of_exp"] + " years")
        if get_neg_data["years_of_exp"] != "":
            self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_neg_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting errorneous date from text input: " + get_neg_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_neg_data["date_of_birth"])
        
        # click submit button
        logger.info("Sumitting form...")
        form_page.retrieve_loc_btn_submit().click()
        
        # Assert success message is seen on the alert element
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()