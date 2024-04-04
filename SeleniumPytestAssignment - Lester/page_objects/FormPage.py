"""
    Module contains the locators for the form page.
    - WebDriver object is present only upon object initialization
    - Locators are stored as static variables
        - Demonstrating understanding of the different ways to locate
            - ID, CLASSNAME, XPATH, CSSSelector
    - Getter methods define the calling of locators and returning them as WebElement
"""
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class FormPage():
    
    loc_txtFirstName: WebElement = (By.ID, "first-name")
    loc_txtLastName: WebElement = (By.XPATH, "//input[@placeholder='Enter last name']")
    loc_txtJobTitle: WebElement = (By.CSS_SELECTOR, "#job-title")
    # loc_radioEduLevel: List[WebElement]  = (By.XPATH, "//input[@aria-label='Radio button']")
    loc_radioEduLevel: WebElement = (By.XPATH, "//body/div[1]/form[1]/div[1]/div[4]")
    # loc_chkSex: List[WebElement] = (By.CSS_SELECTOR, "input[aria-label='checkbox']")
    loc_chkSex: WebElement = (By.XPATH, "//body/div[1]/form[1]/div[1]/div[5]")
    loc_select_YearsOfExp: WebElement = (By.ID, "select-menu")
    loc_txtdtpicker_DateCalendar: WebElement = (By.ID, "datepicker")
    loc_btnSubmit: WebElement = (By.LINK_TEXT, "Submit")
    loc_alert: WebElement = (By.CLASS_NAME, "alert")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def retrieve_loc_txt_first_name(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_txtFirstName)
    
    def retrieve_loc_txt_last_name(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_txtLastName)
    
    def retrieve_loc_txt_job_title(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_txtJobTitle)
    
    def retrieve_loc_radio_edu_level(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_radioEduLevel)
    
    def retrieve_loc_chkSex(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_chkSex)
    
    def retrieve_loc_select_years_of_exp(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_select_YearsOfExp)
    
    def retrieve_loc_txt_dt_datepicker(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_txtdtpicker_DateCalendar)
    
    def retrieve_loc_btn_submit(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_btnSubmit)
    
    def retrieve_loc_alert(self) -> WebElement:
        return self.driver.find_element(*FormPage.loc_alert)