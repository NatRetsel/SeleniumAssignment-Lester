"""
    This module contains the negative test case class for the checkbox fields in the form page
    The user:
        - Upon clicking extra or wrong boxes, should be able to uncheck their previous choices
        - Should not be seeing success when submitting a form with multiple or no check boxes selected
            - Checkbox field should be marked as required
            - A person's sex should not be of multiple values
    
    Upon clicking extra or wrong boxes, should be able to uncheck their previous choices
        We will validate that the previous button value is unchecked and only the button with that 
        latest value is checked. Test data will come from in test_data.FormPageDataPartialNegative: List[Dict].
    
    Should not be seeing success when submitting a form with multiple or no check boxes selected
        - Checkbox field should be marked as required
            - Form is submitted with other fields filled properly and with checkbox field untouhed
        - A person's sex should not be of multiple values
            - Form is submitted with other fields filled properly and with multiple checkbox selected
    
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
from test_data.FormPageDataNegative import FormPageDataPartialNegative
from pytest_check import check
from _pytest.fixtures import FixtureRequest
from typing import Dict
import logging

class TestFormPageChkNegative(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    
    @pytest.fixture(params=FormPageDataPartialNegative.test_form_data)
    def get_partial_neg_data(self, request: FixtureRequest):
        return request.param
    

    def test_chk_sex_unchecking_negative(self, get_partial_neg_data: Dict):
        # Method retrieves checkbox element for sex and 
        # first selects one option, it then tries to unselect it and selects the next option
        # verify that only the latest option is selected
        logger: logging.Logger = self.getLogger()
        fields:set = {"Male", "Female", "Prefer not to say"}
        form_page:FormPage = FormPage(self.driver)
        
        logger.info("Checking and checking checkboxes for sex: " + str(get_partial_neg_data["sex"]))
        for i in range(len(get_partial_neg_data["sex"])):
            # Check
            self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_partial_neg_data["sex"][i])
            # uncheck except if it is the last option
            if i != len(get_partial_neg_data["sex"])-1:
                self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_partial_neg_data["sex"][i])
        
        logger.info("Asserting only the latest option remain selected: " + get_partial_neg_data["sex"][-1])
        for field in fields:
            if (field != get_partial_neg_data["sex"][-1]):
                assert not form_page.retrieve_loc_chkSex().find_element(By.XPATH, "div[normalize-space()='"+field+"']/input").is_selected() and form_page.retrieve_loc_chkSex().find_element(By.XPATH, "div[normalize-space()='"+get_partial_neg_data["sex"][-1]+"']/input").is_selected()
            
                
        # Refreshes the page for other test cases / data
        self.driver.refresh()
    
    def test_chk_sex_submission_negative(self, get_data: Dict):
        # Method populates other fields with proper data
        # and selects 0 or multiple checkboxes for the sex option.
        
        logger :logging.Logger = self.getLogger()
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
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for: " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        options = ["Male", "Female", "Prefer not to say"]
        # Log the number of options checked with each submission. Won't be asserting for the case of single box checked
        
        for i in range(0, len(options)+1):
            if i == 0: logger.info("Selecting "+str(i)+" checkbox for sex")
            if i > 0:
                logger.info("Selecting "+str(i)+" checkboxes for sex")
                self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), options[i-1])
            if i!=1:
                # click submit button
                logger.info("Submitting form with " + str(i) + " checkboxes selected for sex")
                form_page.retrieve_loc_btn_submit().click()

                logger.info("Asserting alert message after form submission")
                with check:
                    assert "success" not in form_page.retrieve_loc_alert().text
            
                # Goes back to previous page and not refresh to leave other fields filled
                # we will check more buttons next iteration
                self.driver.back()
            else:
                self.driver.refresh()
        
        # Refresh page at the end of each set
        self.driver.refresh()