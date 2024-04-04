"""
    This module contains the negative test case class for the radio fields in the form page
    The user:
        - may select more than one radio button option 
            - reason: user clicked the wrong option initially and there should only be one radio option selected
                - i.e. previous selected option should be unchecked.
            - form submission with this errorneous case should not be a success
        - user submits with no buttons checked (reason: field should be marked as required)
            - all other fields are populated correctly
        
    We will validate that only the most recent button value is checked and the others must be unchecked. 
    Data will come from in test_data.FormPageDataNegative: List[Dict].
    
    We will validate the submission with no radio buttons selected using test_data.FormPageDataPositive: List[Dict]
    for all other fields
    
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataNegative: List[Dict]
    and test_data.FormPageDataPositive: List[Dict] for the test on no radio buttons clicked
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""

import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from selenium.webdriver.common.by import By
from test_data.FormPageDataPositive import FormPageDataPositive
from test_data.FormPageDataNegative import FormPageDataPartialNegative
from pytest_check import check
from typing import Dict, List
from _pytest.fixtures import FixtureRequest
import logging

class TestFormPageRadioBtnPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    @pytest.fixture(params=FormPageDataPartialNegative.test_form_data)
    def get_partial_neg_data(self, request: FixtureRequest):
        return request.param
    
    def test_radio_highest_edu_level_negative(self,get_partial_neg_data: Dict):
        # Method retrieves radio element for highest education level and 
        # selects multiple fields
        # we will check that the only the latest clicked option is selected and all others are unselected
        logger: logging.Logger = self.getLogger()
        fields:set = {"High School", "College", "Grad School"}
        form_page:FormPage = FormPage(self.driver)
        
        logger.info("Selecting multiple education level buttons: " + str(get_partial_neg_data["edu_level"]))
        for option in get_partial_neg_data["edu_level"]:
            self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), option)
        
        logger.info("Asserting that only one radio button remain selected: " + get_partial_neg_data["edu_level"][-1])
        for field in fields:
            if (field != get_partial_neg_data["edu_level"][-1]):
                assert not form_page.retrieve_loc_radio_edu_level().find_element(By.XPATH, "div[normalize-space()='"+field+"']/input").is_selected() and form_page.retrieve_loc_radio_edu_level().find_element(By.XPATH, "div[normalize-space()='"+get_partial_neg_data["edu_level"][-1]+"']/input").is_selected()
        
        
        # Refreshes the page for other test cases / data
        self.driver.refresh()
        
    def test_radio_highest_edu_level_negative_submission(self, get_data: Dict):
        # Method retrieves radio element for highest education level and selects multiple or no fields
        # all other fields are properly filled
        # we will check that submission should not be a success
        logger: logging.Logger = self.getLogger()
        fields: List = ["High School", "College", "Grad School"]
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
        
        # select sex checkbox
        logger.info("Selectiong checkbox for sex: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        # we will log the number of radio buttons checked and submitted for each test case.
        # Won't be asserting for the case of one radio button checked
        
        for i in range(len(fields)+1):
            if i == 0: logger.info("Selecting "+str(i)+" radio buttons for highest education level")
            if i > 0:
                logger.info("Selecting "+str(i)+" radio buttons for highest education level")
                self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), fields[i-1])
            
            if i!=1:
                # click submit button
                logger.info("Submitting form with " + str(i) + " buttons selected for highest education level")
                form_page.retrieve_loc_btn_submit().click()

                logger.info("Asserting alert message after form submission")
                with check:
                    assert "success" not in form_page.retrieve_loc_alert().text
            
                # Goes back to previous page and not refresh to leave other fields filled
                # we will check more buttons next iteration
                self.driver.back()
        
        # Refresh page at the end of each set
        self.driver.refresh()
            
            