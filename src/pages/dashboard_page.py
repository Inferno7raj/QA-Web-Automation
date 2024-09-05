from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager


class UserSearch:

    search_input_field = (By.XPATH,"//input[@class='oxd-input oxd-input--active']")
    username_input_field = (By.XPATH,"//input[@name='username']")
    password_input_field = (By.XPATH,"//input[@name='password']")
    login_button = (By.XPATH,"//button[text()=' Login ']")
    validate_user = (By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']")
    users_about = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    
    admin_button = (By.XPATH,"//span[text()='Admin']")
    username_input_field_on_sys_users = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    username_input_field_on_focus = (By.XPATH,"(//input[@class='oxd-input oxd-input--focus'])")
    
    search_button = (By.XPATH,"//button[text()=' Search ']")
    validate_searched_user = (By.XPATH,"(//div[@class='oxd-table-row oxd-table-row--with-border'])[2]/div[2]")
    
       
    def __init__(self, driver):
        self.driver = driver
        
    def search_for_user(self, username_value):
        
        wait = WebDriverWait(self.driver, 30)                    
        
        wait.until(expected_conditions.visibility_of_element_located(self.admin_button))
        self.driver.find_element(*self.admin_button).click()            
       
        wait.until(expected_conditions.visibility_of_element_located(self.username_input_field_on_sys_users))
        self.driver.find_element(*self.username_input_field_on_sys_users).click()
        time.sleep(2)        
        self.driver.find_element(*self.username_input_field_on_focus).send_keys(username_value)
        time.sleep(2)
        
        wait.until(expected_conditions.visibility_of_element_located(self.search_button))
        self.driver.find_element(*self.search_button).click()
        time.sleep(4)
        
        wait.until(expected_conditions.visibility_of_element_located(self.validate_searched_user))
        username_text = self.driver.find_element(*self.validate_searched_user).text
        
        if (username_value != username_text):
            assert self.driver.find_element(*self.validate_searched_user).is_displayed(), "Entered user is not found in the search results" 
            
        allure.attach(self.driver.get_screenshot_as_png(), name = "search_user_page_screenshot", attachment_type = AttachmentType.PNG)   
        
        
        
        
        
        
        
        
        
        
        