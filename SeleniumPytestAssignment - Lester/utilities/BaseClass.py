"""
    Module contains the base class for test classes to inherit.
    The base class contains the procedures that are common to all test classes.
        i.e
            - select option from dropdown specified by a text argument
            - input text fields with specified text argument.
            - explicit waits
            - logger
    The base class uses the setup fixture so inherited test classes can reference the instantiated WebDriver object
"""
import pytest
import logging
import inspect
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class BaseClass():
    
    
    def click_radio_from_text(self, locator:WebElement, option:str) -> None:
        # Method finds the radio button option given the WebElement locator and String option
        locator.find_element(By.XPATH, "div[normalize-space()='"+option+"']/input").click()
        #        edu_level.find_element(By.XPATH, "input[@type='radio']").click()
    
    
    def click_checkbox_from_text(self, locator:WebElement, option:str) -> None:
        # Method finds the checkbox option given the WebElement locator and String option
        locator.find_element(By.XPATH, "div[normalize-space()='"+option+"']/input").click()
        
        
    def select_dropdown_from_text(self, locator:WebElement, option:str) -> None:
        # Method selects the appropriate choice for a given year(s) of experience
        # It iterates through the options and checks if the user's YOE falls within range of the option before selecting
        dropdown: WebElement = Select(locator)
        options: List[WebElement] = dropdown.options[1:] # We are not interested in "Select an option"
        
        found:bool = False
        for opt in options:
            opt_text:str = opt.text
            pieced_str: str = ""
            left_bound: int = -float('inf')
            right_bound: int = float('inf')
            separator: str = ""
            
            for i in range(0, len(opt_text)):
                if (opt_text[i].isdigit() and (pieced_str == "" or pieced_str.isdigit())):
                    pieced_str += opt_text[i]
                
                elif (not opt_text[i].isdigit()):
                    separator = opt_text[i]
                    left_bound = int(pieced_str)
                    pieced_str = ""
            
            if pieced_str.isdigit():
                right_bound = int(pieced_str)
                
            match separator:
                case "-":
                    if (left_bound <= int(option) <= right_bound):
                        opt.click()
                        found = True
                    
                case "+":
                    opt.click()
                    found = True
                    
            if found: break
            
    def select_calendar_date_from_text(self, locator:WebElement, option:str):
        # Method inputs option into the datepicker and hits return
        # date in the format mm/dd/yyyy
        locator.send_keys(option, Keys.RETURN)
        
    
    def getLogger(self) -> logging.Logger:
        # Method initializes and returns a logging.Logger object
        loggerName: str = inspect.stack()[1][3]
        logger: logging.Logger = logging.getLogger(loggerName) #catches filename

        fileHandler = logging.FileHandler('logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger