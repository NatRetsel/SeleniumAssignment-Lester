"""
    This module contains the positive test data for the form page
    - We will assume the date field to be date of birth
    - We assume the user inputs are valid
        - user will not choose a future date of birth
        - user will not choose a date that does not exist
            - i.e. 30 Feb
    - Additional test case can be added with another dictionary in the list with the appropriate key and values
        
"""
from typing import List, Dict
class FormPageDataPositive():
    test_form_data: List[Dict[str,str]] = [
        {"first_name":"Jon", "last_name":"Tan", "job_title":"Engineer", 
         "edu_level":"College", "sex":"Male", "years_of_exp":"5","date_of_birth":"10/10/1994"},
        
        {"first_name":"Jane", "last_name":"Chua", "job_title":"HR", 
         "edu_level":"High School", "sex":"Female", "years_of_exp":"1","date_of_birth":"10/10/2000"},
        
        {"first_name":"Richard", "last_name":"Milles", "job_title":"CEO", 
         "edu_level":"Grad School", "sex":"Prefer not to say", "years_of_exp":"11","date_of_birth":"10/10/1990"}
    ]