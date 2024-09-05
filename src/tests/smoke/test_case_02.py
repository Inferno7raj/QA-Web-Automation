from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from pages.login_page import LoginPage
from pages.dashboard_page import UserSearch
from pages.add_new_user_page import AddNewUser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
import pytest
import json

class Test_case_02:

    @pytest.mark.usefixtures("setup_teardown")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_02(self):              

        with open(TEST_DATA_DIR + '/test_case_02.json', 'r') as json_file:
            test_data = json.load(json_file)            
            name = test_data['name']
            username = test_data['username']
            password = test_data['password']
                       
            
        wait = WebDriverWait(self.driver, 30)
             
        add_new_user = AddNewUser(self.driver)             
        
        add_new_user.create_user(name, username, password)        
        logging.info("New user is created")
        
        logging.info("Workflow Completed")