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

class AddNewUser:
    
    admin_button = (By.XPATH,"//span[text()='Admin']")
    add_new_user_button = (By.XPATH,"//button[text()=' Add ']")
    user_role_select = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
    select_admin_option = (By.XPATH,"//div[@class='oxd-select-text oxd-select-text--focus']/following-sibling::div[1]")
    status_select = (By.XPATH,"(//div[@class='oxd-select-text--after'])[2]")
    enabled_option = (By.XPATH,"//div[@class='oxd-select-text oxd-select-text--focus']/following-sibling::div[1]")
    employee_name_input_field = (By.XPATH,"//input[@placeholder='Type for hints...']")
    username_input_field_on_add_users = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    username_input_field_add_userfocus = (By.XPATH,"(//input[@class='oxd-input oxd-input--focus'])")
    password_input_field = (By.XPATH,"(//input[@type='password'])[1]")
    confirm_password_input_field = (By.XPATH,"(//input[@type='password'])[2]")
    save_button = (By.XPATH,"//button[@type='submit']")
    
    
       
    def __init__(self, driver):
        self.driver = driver
        
    def create_user(self,name, username, password):
        
        wait = WebDriverWait(self.driver, 30)                                     
        
        wait.until(expected_conditions.visibility_of_element_located(self.admin_button))
        self.driver.find_element(*self.admin_button).click()  
        
        wait.until(expected_conditions.visibility_of_element_located(self.add_new_user_button))
        self.driver.find_element(*self.add_new_user_button).click()  
        
        wait.until(expected_conditions.visibility_of_element_located(self.user_role_select))
        self.driver.find_element(*self.user_role_select).click()  
       
        wait.until(expected_conditions.visibility_of_element_located(self.select_admin_option))
        self.driver.find_element(*self.select_admin_option).click() 
                
        wait.until(expected_conditions.visibility_of_element_located(self.status_select))
        self.driver.find_element(*self.status_select).click() 
                        
        wait.until(expected_conditions.visibility_of_element_located(self.enabled_option))
        self.driver.find_element(*self.enabled_option).click() 
                
        wait.until(expected_conditions.visibility_of_element_located(self.employee_name_input_field))
        self.driver.find_element(*self.employee_name_input_field).click()
        time.sleep(2)        
        self.driver.find_element(*self.employee_name_input_field).send_keys(name)
        time.sleep(2)
         
        wait.until(expected_conditions.visibility_of_element_located(self.username_input_field_on_add_users))
        self.driver.find_element(*self.username_input_field_on_add_users).click()
        time.sleep(2)        
        self.driver.find_element(*self.username_input_field_add_userfocus).send_keys(username)
        time.sleep(2)
        
        wait.until(expected_conditions.visibility_of_element_located(self.password_input_field))
        self.driver.find_element(*self.password_input_field).click()
        time.sleep(2)        
        self.driver.find_element(*self.username_input_field_add_userfocus).send_keys(password)
        time.sleep(2)
        
        wait.until(expected_conditions.visibility_of_element_located(self.confirm_password_input_field))
        self.driver.find_element(*self.confirm_password_input_field).click()
        time.sleep(2)        
        self.driver.find_element(*self.confirm_password_input_field).send_keys(password)
        time.sleep(2)
                
        wait.until(expected_conditions.visibility_of_element_located(self.save_button))
        self.driver.find_element(*self.save_button).click()
        time.sleep(2)  
        
        allure.attach(self.driver.get_screenshot_as_png(), name = "create_user_page_screenshot", attachment_type = AttachmentType.PNG)   