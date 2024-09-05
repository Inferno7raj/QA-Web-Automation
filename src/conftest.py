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


@pytest.fixture(scope="function")
def setup_teardown(request): 

    options = webdriver.ChromeOptions()
    options.use_chromium = True

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    options.add_experimental_option("prefs",{"download.default.directory":DOWNLOAD_DIR})
    options.add_experimental_option("prefs", {"download.prompt_for_download": False})
    options.add_argument("--disable-notifications")    
      
    driver.implicitly_wait(40)

    driver.get(site_url)
    driver.maximize_window()
    request.cls.driver = driver

    login_page = LoginPage(driver)      
    logout_Page = LogoutPage(driver)

    wait = WebDriverWait(driver, 30)

    decoded_username = decode(username)
    decoded_password = decode(password)         
    
    wait.until(expected_conditions.visibility_of_element_located(login_page.username_input_field))
    driver.find_element(*login_page.username_input_field).click()
    driver.find_element(*login_page.username_input_field).send_keys(decoded_username)
    
    wait.until(expected_conditions.visibility_of_element_located(login_page.password_input_field))
    driver.find_element(*login_page.password_input_field).click()
    driver.find_element(*login_page.password_input_field).send_keys(decoded_password)
        
    wait.until(expected_conditions.visibility_of_element_located(login_page.login_button))
    driver.find_element(*login_page.login_button).click()  
    time.sleep(4)             
               
    wait.until(expected_conditions.visibility_of_element_located(login_page.validate_user))
    user_text = driver.find_element(*login_page.validate_user).text    
    
    if (user_text != 'Dashboard'):
        assert driver.find_element(*login_page.validate_user).is_displayed(), "The user is not logged in with the given login credentials."    

    allure.attach(driver.get_screenshot_as_png(), name = "login_page_screenshot", attachment_type = AttachmentType.PNG)
    logging.info(f"User is logged in with {decoded_username} username")
    
    yield
    allure.attach(driver.get_screenshot_as_png(), name = "last_active_page_screenshot", attachment_type = AttachmentType.PNG)    
    wait.until(expected_conditions.visibility_of_element_located(logout_Page.logout_dropdown))
    driver.find_element(*logout_Page.logout_dropdown).click()  
    
    wait.until(expected_conditions.visibility_of_element_located(logout_Page.log_out_icon))
    driver.find_element(*logout_Page.log_out_icon).click()  
    
    driver.quit()
    logging.info("Closed the driver session.")

    @pytest.hookimpl(trylast = True)
    def pytest_configure(config):
        allure.environment(test_server = '127.0.0.1', report = 'My Test Report')



    

