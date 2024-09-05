from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LoginPage:

    login_icon = (By.XPATH,"//a[text() = 'Log in']")
    username_input_field = (By.XPATH,"//input[@name='username']")
    password_input_field = (By.XPATH,"//input[@name='password']")
    login_button = (By.XPATH,"//button[text()=' Login ']")
    validate_user = (By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']")
    
       
    def __init__(self, driver):
	    self.driver = driver
