from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LogoutPage:

    logout_dropdown = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    log_out_icon = (By.XPATH,"//a[text()='Logout']")
    
    
    
    def __init__(self, driver):
	    self.driver = driver
