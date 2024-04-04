"""
    This module contains the negative test data for the form page
    - We will assume the date field to be date of birth
    - We assume the user inputs are invalid
        - user might choose a future date of birth than current date
        - user may select more than one radio button
        - user may select more than one check box
        - user leaving fields blank
    - Additional test case can be added with another dictionary in the list with the appropriate key and values
    
    - Partial negative omits cases with empty fields for radio and checkboxes
        
"""
from typing import List, Dict
class FormPageDataPartialNegative():
    test_form_data: List[Dict] = [
        {"first_name":"Jon", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"Jane", "last_name":"Chua", "job_title":"HR", 
         "edu_level":["High School", "Grad School"], "sex":["Female", "Prefer not to say"], "years_of_exp":"1","date_of_birth":"10/10/2027"},
        
        {"first_name":"Richard", "last_name":"Milles", "job_title":"CEO", 
         "edu_level":["Grad School", "College"], "sex":["Prefer not to say", "Male"], "years_of_exp":"11","date_of_birth":"10/10/3000"},
        
        {"first_name":"", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"", "last_name":"", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"Jon", "last_name":"Tan", "job_title":"", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"}
    ]
    
class FormPageDataNegative():
    test_form_data: List[Dict] = [
        {"first_name":"Jon", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"Jane", "last_name":"Chua", "job_title":"HR", 
         "edu_level":["High School", "Grad School"], "sex":["Female", "Prefer not to say"], "years_of_exp":"1","date_of_birth":"10/10/2027"},
        
        {"first_name":"Richard", "last_name":"Milles", "job_title":"CEO", 
         "edu_level":["Grad School", "College"], "sex":["Prefer not to say", "Male"], "years_of_exp":"11","date_of_birth":"10/10/3000"},
        
        {"first_name":"", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"", "last_name":"", "job_title":"Engineer", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"Jon", "last_name":"Tan", "job_title":"", 
         "edu_level":["College", "High School"], "sex":["Male", "Female"], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"Jon", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":[], "sex":[], "years_of_exp":"5","date_of_birth":"10/10/9999"},
        
        {"first_name":"", "last_name":"", "job_title":"", 
         "edu_level":[], "sex":[], "years_of_exp":"","date_of_birth":""}
    ]