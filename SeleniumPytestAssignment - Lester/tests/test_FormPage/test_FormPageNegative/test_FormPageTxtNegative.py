"""
    This module contains the negative test case class for the text input fields in the form page.
    Will check that the alert shouldn't be success when form is submitted:
        - with empty name fields (reason: field should be marked as required)
        - with a future date of birth (reason: DOB cannot be in the future at time of filling)
    
    Webdriver is assessible from the parent class having decorated with the setup and teardown fixtures
    The tests will be done with multiple datasets stored in test_data.FormPageDataPositive: List[Dict]
        - tests on each set of data are controlled by parameterized fixture in the form of a dictionary
    
    We use positive test case to show the example when all other fields are populated except the
    field in question as well as hardcoding negative inputs while leaving other fields positive
    
    Locators to the form page is accessible from the Page Object in page_objects.FormPage
"""
import pytest
from utilities.BaseClass import BaseClass
from page_objects.FormPage import FormPage
from test_data.FormPageDataPositive import FormPageDataPositive
from pytest_check import check
from typing import Dict
from _pytest.fixtures import FixtureRequest
import logging

class TestFormPageTxTPositive(BaseClass):
    
    @pytest.fixture(params=FormPageDataPositive.test_form_data)
    def get_data(self, request: FixtureRequest):
        return request.param
    
    
    def test_txt_first_name_negative(self, get_data: Dict):
        # Method submits without filling up first name field
        # all other fields are populated correctly
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
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
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        # click submit button with empty name field
        logger.info("Sumitting form with empty first name field")
        form_page.retrieve_loc_btn_submit().click()
        
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()
    
    
    def test_txt_last_name_negative(self, get_data: Dict):
        # Method submits without filling up last name field
        # all other fields are populated correctly
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate first name
        logger.info("Populating first name: " + get_data["first_name"])
        form_page.retrieve_loc_txt_first_name().send_keys(get_data["first_name"])
        
        # populate job title
        logger.info("Populating job title: " + get_data["job_title"])
        form_page.retrieve_loc_txt_job_title().send_keys(get_data["job_title"])
        
        
        # select radio option
        logger.info("Selecting radio button for highest education level: " + get_data["edu_level"])
        self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), get_data["edu_level"])
        
        # select sex checkbox
        logger.info("Selectiong checkbox for sex: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        
        # click submit button with empty name field
        logger.info("Sumitting form with empty last name field")
        form_page.retrieve_loc_btn_submit().click()
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()
        
        
    def test_txt_job_title_negative(self, get_data: Dict):
        # Method submits without filling up job title field
        # all other fields are populated correctly
        logger: logging.Logger = self.getLogger()
        form_page:FormPage = FormPage(self.driver)
        
        # populate first name
        logger.info("Populating first name: " + get_data["first_name"])
        form_page.retrieve_loc_txt_first_name().send_keys(get_data["first_name"])
        
        
        # populate last name
        logger.info("Populating last name: " + get_data["last_name"])
        form_page.retrieve_loc_txt_last_name().send_keys(get_data["last_name"])
        
        # select radio option
        logger.info("Selecting radio button for highest education level: " + get_data["edu_level"])
        self.click_radio_from_text(form_page.retrieve_loc_radio_edu_level(), get_data["edu_level"])
        
        # select sex checkbox
        logger.info("Selectiong checkbox for sex: " + get_data["sex"])
        self.click_checkbox_from_text(form_page.retrieve_loc_chkSex(), get_data["sex"])
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting date from text input: " + get_data["date_of_birth"])
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), get_data["date_of_birth"])
        
        # click submit button with empty job field
        logger.info("Sumitting form with empty job title field")
        form_page.retrieve_loc_btn_submit().click()
        
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()
        
    def test_txt_datepicker_empty_negative(self, get_data: Dict):
        # Method submits without filling the date field
        # other fields are populated
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
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # click submit button
        logger.info("Sumitting form with empty date field")
        form_page.retrieve_loc_btn_submit().click()
        
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()
        
        
    def test_txt_datepicker_negative(self, get_data: Dict):
        # Method populates date field (assumed to be date of birth) with dates in the future
        # while leaving the other fields positively filled.
        
        # Method submits without filling the date field
        # other fields are populated
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
        
        # select YOE drop down
        logger.info("Selecting years of experience from dropdown for " + get_data["years_of_exp"] + " years")
        self.select_dropdown_from_text(form_page.retrieve_loc_select_years_of_exp(), get_data["years_of_exp"])
        
        # select date by send_keys
        logger.info("Selecting errorneous date from text input: 10/10/9999")
        self.select_calendar_date_from_text(form_page.retrieve_loc_txt_dt_datepicker(), "10/10/9999") #errorneous date
        
        # click submit button
        logger.info("Sumitting form with errorneous date")
        form_page.retrieve_loc_btn_submit().click()
        logger.info("Asserting alert after submission")
        with check:
            assert "success" not in form_page.retrieve_loc_alert().text
        
        # Goes back to previous page and refreshes so other tests can proceed
        self.driver.back()
        self.driver.refresh()